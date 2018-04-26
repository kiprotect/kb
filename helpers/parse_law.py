import roman
import sys
import re
import os

from law_exporter import store_result
from law_indexer import build_index

stopwords = {
    'en' : {
        'chapter' : 'CHAPTER',
        'article' : 'Article',
        'section' : 'Section',
        'paragraph_regex_capture' : r'([\d]+)\.',
        'paragraph_regex' : r'[\d]+\.',
        'definition_regex_capture' : r'\(([\d]+)\)',
        'definition_regex' : r'\([\d]+\)',
    },
    'de' : {
        'chapter' : 'KAPITEL',
        'article' : 'Artikel',
        'section' : 'Abschnitt',
        'paragraph_regex_capture' : r'\(([\d]+)\)',
        'paragraph_regex' : r'\([\d]+\)',
        'definition_regex_capture' : r'([\d]+)\.',
        'definition_regex' : r'[\d]+\.',
    }
}

class Parser(object):

    def __init__(self, stopwords):
        self.regexes = {
            'chapter' : re.compile(r'^(.*?){chapter}\s+([\w]+)\n(.*?)((?:\n{chapter}\s+\w+\n.*$)|$)'.format(**stopwords), re.S),
            'section' : re.compile(r'^(.*?){section}\s+([\d]+)\n(.*?)((?:\n{section}\s+\d+\n.*$)|$)'.format(**stopwords), re.S),
            'article' : re.compile(r'^(.*?){article}\s+([\d]+)\n(.*?)((?:\n{article}\s+\d+\n.*$)|$)'.format(**stopwords), re.S),
            'recital' : re.compile(r'^(.*?)\(([\d]+)\)\n(.*?)((?:\n\(\d+\)\s*\n.*$)|$)', re.S),
            'footnote' : re.compile(r'^(.*?)\(([\d]+)\)\s+(.*?)((?:\n\(\d+\)\s+.*$)|$)', re.S),
            'paragraph' : re.compile(r'^(.*?)\n{paragraph_regex_capture}(.*?)((?:\n{paragraph_regex}.*$)|$)'.format(**stopwords), re.S),
            'definition' : re.compile(r'^(.*?)\n{definition_regex_capture}(.*?)((?:\n{definition_regex}.*$)|$)'.format(**stopwords), re.S),
            'simple_article' : re.compile(r'^\s*(.*)$', re.S),
            'article_title' : re.compile(r'^\s*\n([^\n]+)(\n+.*)$', re.S),
            'point' : re.compile(r'^(.*?)\n\(?([\w]+)\)\n+([^\n].*?)((?:\n\(?\w+\).*$)|$)', re.S),
            'sanitize' : re.compile(r'\s+'),
        }

    def parse(self, articles, recitals, footnotes):
        return {
            'chapters' : self.parse_chapters(articles),
            'recitals' : self.parse_recitals(recitals),
            'footnotes' : self.parse_footnotes(footnotes),
        }

    def parse_recitals(self, s):
        recitals = {}
        while s:
            match = self.regexes['recital'].match(s)
            if not match:
                raise ValueError("Invalid suffix!")
            prefix, number, content, suffix = match.groups()
            number = int(number)
            recitals[number] = self.parse_recital(content, number)
            s = suffix
        return recitals

    def parse_recital(self, s, number):
        return {'content' : self.sanitize(s), 'number' : number}

    def parse_footnotes(self, s):
        footnotes = {}
        while s:
            match = self.regexes['footnote'].match(s)
            if not match:
                raise ValueError("Invalid suffix!")
            prefix, number, content, suffix = match.groups()
            number = int(number)
            footnotes[number] = self.parse_footnote(content, number)
            s = suffix
        return footnotes

    def parse_footnote(self, s, number):
        return {'content' : self.sanitize(s), 'number' : number}

    def sanitize(self, s):
        s = s.strip()
        s = self.regexes['sanitize'].sub(' ', s)
        return s

    def parse_chapters(self, s):
        chapters = {}
        while s:
            match = self.regexes['chapter'].match(s)
            if not match:
                raise ValueError("Invalid suffix!")
            prefix, number, content, suffix = match.groups()
            converted_number = roman.fromRoman(number)
            chapters[converted_number] = self.parse_chapter(content, converted_number)
            chapters[converted_number]['roman_number'] = number
            s = suffix
        return chapters

    def parse_chapter(self, s, number):
        sections = {}
        chapter = {
            'number' : number
        }
        while s:
            match = self.regexes['section'].match(s)
            if not match:
                sections[0] = self.parse_section(s, 0)
                chapter['title'] = sections[0]['title']
                del sections[0]['title']
                break
            prefix, number, content, suffix = match.groups()
            number = int(number)
            sections[number] = self.parse_section(content, number)
            if not 'title' in chapter:
                chapter['title'] = self.sanitize(prefix)
            s = suffix
        if sections:
            chapter['sections'] = sections
        return chapter

    def parse_section(self, s, number):
        articles = {}
        section = {
            'articles' : articles,
            'number' : number
        }
        while s:
            match = self.regexes['article'].match(s)
            if not match:
                raise ValueError("Invalid suffix!")
            prefix, number, content, suffix = match.groups()
            number = int(number)
            articles[number] = self.parse_article(content, number)
            if not 'title' in section:
                section['title'] = self.sanitize(prefix)
            s = suffix
        return section

    def parse_article(self, s, number):
        elements = {}
        article = {
            'number' : number
        }
        match = self.regexes['article_title'].match(s)
        if not match:
            raise ValueError("Article without title!")
        title, content = match.groups()
        article['title'] = self.sanitize(title)
        s = content

        paragraph_match = self.regexes['paragraph'].match(s)
        point_match = self.regexes['point'].match(s)
        definition_match = self.regexes['definition'].match(s)
        is_number = False
        if paragraph_match:
            relevant_regex = self.regexes['paragraph']
            key = 'paragraphs'
            is_number = True
        elif definition_match:
            key = 'definitions'
            relevant_regex = self.regexes['definition']
            is_number = True
        elif point_match:
            key = 'points'
            relevant_regex = self.regexes['point']
        else: #this is a simple article
            match = self.regexes['simple_article'].match(s)
            if not match:
                raise ValueError("Cannot match article!")
            content, = match.groups()
            article['content'] = self.sanitize(content)
            return article
        while s:
            match = relevant_regex.match(s)
            if not match:
                raise ValueError("Invalid suffix!")
            prefix, number, content, suffix = match.groups()
            if is_number:
                number = int(number)
            elements[number] = self.parse_paragraph(content, number)
            prefix = self.sanitize(prefix)
            if (not 'preamble' in article) and prefix:
                article['preamble'] = prefix
            s = suffix
        if elements:
            article[key] = elements
        return article

    def parse_paragraph(self, s, number):
        points = {}
        paragraph = {
            'number' : number,
        }
        matched = False
        while s:
            match = self.regexes['point'].match(s)
            if not match:
                if s.strip().startswith("(g)"):
                    sys.stderr.write(s+"\n")
                if not matched:
                    key = 'content'
                else:
                    key = 'suffix'
                paragraph[key] = self.sanitize(s)
                break
            matched = True
            prefix, number, content, suffix = match.groups()
            points[number] = self.parse_point(content)
            if not 'preamble' in paragraph:
                paragraph['preamble'] = self.sanitize(prefix)
            s = suffix
        if points:
            paragraph['points'] = points
        return paragraph

    def parse_point(self, s):
        return {
            'content' : self.sanitize(s)
        }

if __name__ == '__main__':
    if len(sys.argv) < 5:
        sys.stderr.write("Usage: {} [articles.txt] [recitals.txt] [footnotes.txt] [build dir] [lang|en]\n".format(sys.argv[0]))
        exit(-1)
    articles, recitals, footnotes, build_dir = sys.argv[1:5]
    if len(sys.argv) >= 6:
        lang = sys.argv[5]
    else:
        lang = 'en'
    parser = Parser(stopwords[lang])
    with open(articles) as articles_file:
        articles_content = articles_file.read()
    with open(recitals) as recitals_file:
        recitals_content = recitals_file.read()
    with open(footnotes) as footnotes_file:
        footnotes_content = footnotes_file.read()
    result = parser.parse(articles_content, recitals_content, footnotes_content)
    index = build_index(result, lang)
    build_dir = os.path.abspath(build_dir)
    store_result(result, build_dir)
