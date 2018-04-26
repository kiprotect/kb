from beam.builders.base import BaseBuilder

from collections import defaultdict

import re
import os

import logging

logger = logging.getLogger(__name__)

def crawl_index(d):
    for key, value in d.items():
        if isinstance(value, dict):
            for result in crawl_index(value):
                yield result
        if key == 'index':
            for index_value in value:
                yield index_value

def group_definitions(sorted_definitions):
    packs = []
    i = 0
    a = 0
    di = 5
    previous_letters = None
    while i < len(sorted_definitions):
        pack = sorted_definitions[i:i+di]
        i += di
        if not pack:
            break
        first_definition = pack[0][1]
        last_definition = pack[-1][1]
        current_length = 1
        first_letters = first_definition['title'][:current_length]
        if previous_letters:
            while first_letters[:current_length] == previous_letters[:current_length]:
                current_length += 1
                first_letters = first_definition['title'][:current_length]
        current_length = 1
        while True:
            last_letters = last_definition['title'][:current_length]
            if last_letters[:current_length] == first_letters[:current_length]:
                current_length += 1
            else:
                break
        current_length = 1
        #we check the next character that we would get
        if i < len(sorted_definitions):
            _, next_definition = sorted_definitions[i]
            next_letters = last_definition['title'][:current_length]
            while next_letters[:current_length] == last_letters[:current_length]:
                current_length += 1
                last_letters = last_definition['title'][:current_length]
        previous_letters = last_letters
        packs.append({
            'from' : first_letters,
            'to' : last_letters,
            'definitions' : pack,
            'i' : a
        })
        a += 1
    return packs


class LawBuilder(BaseBuilder):

    def __init__(self, site):
        super().__init__(site)
        self.articles_by_language = {}
        self.index_by_language = {}
        self.chapters_by_language = {}
        self.sections_by_language = {}
        self.slugs_by_language = {}
        self.addons = {
            'jinja-filters' : [
                ('law_markup', self.parse_markup),
            ]
        }

    def get_law(self, language):
        return self.site.config['languages'][language]['law']

    def index(self, params, language):
        print("Generating index for law pages and language {}!".format(language))
        return {
            'links' : self.create_links(self.get_law(language), language)
        }

    def create_links(self, law, language):
        self.articles_by_language[language] = {}
        self.index_by_language[language] = {}
        index = defaultdict(set)
        c = {
            'gdpr_name' : self.site.translate(language, 'gdpr').lower(),
            'chapter_name' : self.site.translate(language, 'chapter').lower(),
            'article_name' : self.site.translate(language, 'article').lower(),
            'section_name' : self.site.translate(language, 'section').lower(),
            'wiki_name' : self.site.translate(language, 'wiki').lower(),
            'summary_name' : self.site.translate(language, 'summary').lower(),
            'q_and_a_name' : self.site.translate(language, 'q-and-a').lower(),
            'index_overview' : self.site.translate(language, 'index-overview').lower()
        }

        self.slugs_by_language[language] = {
            'articles-overview' : '{gdpr_name}/index'.format(**c),
            'index-overview' : '{gdpr_name}/{index_overview}'.format(**c)
        }

        links = {
            'gdpr-articles-overview' : self.site.get_link_dst(self.slugs_by_language[language]['articles-overview'], language),
            'gdpr-index-overview' : self.site.get_link_dst(self.slugs_by_language[language]['index-overview'], language)
        }

        for chapter in law['chapters']:
            for section in chapter['sections']:
                for article in section['articles']:
                    cd = {
                        'chapter' : chapter['roman_number'],
                        'section' : section['number'],
                        'article' : article['number']
                    }
                    cd.update(c)
                    if section['number'] == 0:
                        name = 'gdpr-article-{article}'.format(**cd)
                        slug = '{gdpr_name}/{chapter_name}-{chapter}/{article_name}-{article}'.format(**cd).lower()
                    else:
                        name = 'gdpr-article-{article}'.format(**cd)
                        slug = '{gdpr_name}/{chapter_name}-{chapter}/{section_name}-{section}/{article_name}-{article}'.format(**cd).lower()

                    wiki_name = name + '-wiki'
                    wiki_slug = slug + '/{wiki_name}'.format(**c)
                    summary_name = name + '-summary'
                    summary_slug = slug + '/{summary_name}'.format(**c)

                    for entry in crawl_index(article):
                        index[name].add(entry)
                    obj = {
                        'title' : '{} {} {}'.format(
                            self.site.translate(language, 'gdpr'),
                            self.site.translate(language, 'article'),
                            article['number']),
                        'type' : 'html',
                        'data' : article,
                        'name' : name,
                        'slug' : slug,
                        'wiki_slug' : wiki_slug,
                        'wiki_name' : wiki_name,
                        'summary_slug' : summary_slug,
                        'summary_name' : summary_name,
                    }
                    self.articles_by_language[language][name] = obj
                    links[name] = self.site.get_link_dst(slug, language)
                    links[wiki_name] = self.site.get_link_dst(wiki_slug, language)
                    links[summary_name] = self.site.get_link_dst(summary_slug, language)

        index_objs = {}
        index_name = self.site.translate(language, 'index').lower()

        def get_index_name(value):
            return 'gdpr-index-{}'.format(value)

        def get_index_slug(value):
            return '{gdpr_name}/{index_name}/{value}'.format(index_name=index_name, value=value, gdpr_name=c['gdpr_name'])

        for key, values in index.items():
            for value in values:
                name = get_index_name(value)
                if value in index_objs:
                    obj = index_objs[value]
                    obj['article-references'][key] = self.articles_by_language[language][key]
                    continue
                slug = get_index_slug(value)
                obj = {
                    'type' : 'html',
                    'name' : name,
                    'article-references' : {
                        key : self.articles_by_language[language][key]
                    },
                    'slug' : slug,
                    'value' : value,
                }
                index_objs[value] = obj
                links[name] = self.site.get_link_dst(slug, language)

        #we also include index entries that are not referenced anywhere...
        definitions = law['index']
        for value, definition in definitions.items():
            slug = get_index_slug(value)
            if 'index-name' in definition:
                name = get_index_name(definition['index-name'])
                links[name] = self.site.get_link_dst(slug, language)
            else:
                name = get_index_name(value)
            if value in index_objs:
                #we prefer the index-name for the page name as this will make
                #it possible to switch between different languages...
                if 'index-name' in definition:
                    index_objs[value]['name'] = name
                continue
            obj = {
                'name' : name,
                'slug' : slug,
                'type' : 'html',
                'article-references' : {},
                'value' : value,
            }
            index_objs[value] = obj
            dst = self.site.get_link_dst(slug, language)
            links[name] = dst

        self.index_by_language[language] = index_objs
        return links

    def parse_markup(self, c, language, remove=False):
        regex = re.compile(r'\{([^\}\|]+)\|([^:]+):([^\}]+)\}', re.I)
        def sub(match):
            content, name, value = match.groups()
            if remove:
                return content
            if name == 'index':
                law = self.get_law(language)
                definitions = law['index']
                index = self.index_by_language[language]
                if not value in definitions or not value in index:
                    return content
                obj = index[value]
                link = self.site.href(language, obj['name'])
                return '<a class="index" href="{link}">{content}</a>'.format(link=link, content=content, value=value)
            return match.group(0)
        return regex.sub(sub, c)

    def build_articles_overview(self, language, articles):
        law = self.get_law(language)
        input = self.site.load(law['templates']['articles_overview'])
        vars = {
            'articles' : articles,
            'article' : {}, #we need a dummy object otherwise Jinja complains
            'law' : law,
            'title' : self.site.translate(language, 'articles-overview')
        }
        output = self.site.process(input, {'type' : 'html', 'name' : 'gdpr-articles-overview'}, vars, language)
        filename = self.site.get_dst(self.slugs_by_language[language]['articles-overview'], language)
        self.site.write(output, filename)

    def build_articles(self):
        for language, articles in self.articles_by_language.items():
            self.build_articles_overview(language, articles)
            for name, article in articles.items():
                self.build_article(article, language)

    def build_index_overview(self, language, index, law, sorted_definitions, grouped_definitions):

        input = self.site.load(law['templates']['index_overview'])

        vars = {
            'index' : index,
            'definition' : {}, #we need a dummy object otherwise Jinja complains
            'definitions' : sorted_definitions,
            'grouped_definitions' : grouped_definitions,
            'law' : law,
            'title' : self.site.translate(language, 'index-overview')
        }
        output = self.site.process(input, {'type' : 'html', 'name' : 'gdpr-index-overview'}, vars, language)
        filename = self.site.get_dst(self.slugs_by_language[language]['index-overview'], language)
        self.site.write(output, filename)

    def build_index(self):

        for language, index in self.index_by_language.items():

            law = self.get_law(language)
            definitions = law['index'].items()
            sorted_definitions = sorted(definitions, key=lambda x:x[1].get('title',''))
            grouped_definitions = group_definitions(sorted_definitions)

            self.build_index_overview(language, index, law, sorted_definitions, grouped_definitions)
            for name, obj in index.items():
                self.build_index_page(language, obj, law, sorted_definitions, grouped_definitions)

    def build_index_page(self, language, obj, law, sorted_definitions, grouped_definitions):
        definition = law['index'].get(obj['value'], {})
        if not definition:
            logger.warning("Index for word {}(name:{}) and language {} not found".format(obj['value'], obj['name'], language))
        definition['name'] = obj['value']
        #we set the group of the definition (to allow opening the right entries on the nav menu)
        for group in grouped_definitions:
            for name, d in group['definitions']:
                if name == definition['name']:
                    definition['group'] = group['i']
        vars = {
            'law' : law,
            'definition' : definition,
            'definitions' : sorted_definitions,
            'grouped_definitions' : grouped_definitions,
            'title' : definition.get('title',''),
        }
        input = self.site.load(law['templates']['index_page'])
        output = self.site.process(input, obj, vars, language)
        filename = self.site.get_dst(obj['slug'], language)
        self.site.write(output, filename)


    def build(self):
        self.build_articles()
        self.build_index()

    def build_article(self, article, language):
        law = self.get_law(language)

        vars = {
            'article' : article['data'],
            'law' : law,
            'tab' : 'article',
            'title' : article['title'],
        }
        input = self.site.load(law['templates']['article'])
        output = self.site.process(input, article, vars, language)
        filename = self.site.get_dst(article['slug'], language)
        self.site.write(output, filename)

        self.build_md_addon('wiki', law, article, language)
        self.build_md_addon('summary', law, article, language)

    def build_md_addon(self, name, law, article, language):

        law_dir = law.get('dir', '')

        d = {
            'dir' : law_dir,
            'chapter' : article['data']['chapter'],
            'section' : article['data']['section'],
            'number' : article['data']['number'],
            'name' : name,
        }
        src_path = '{dir}/chapters/{chapter}/sections/{section}/articles/{number}-{name}.md'.format(**d)
        full_src_path = self.site.get_src_path(src_path)

        repo_url = self.site.config.get('repo-url')
        edit_url = '{}/blob/master/{}/{}'.format(repo_url, self.site.src_path, src_path)
        new_url = '{}/blob/master/README{}.md#{}'.format(repo_url, '-{}'.format(language.upper()) if language != 'en' else '', name)

        vars = {
            'article' : article['data'],
            'law' : law,
            'tab' : name,
            'edit_url' : edit_url,
            'new_url' : new_url,
            'title' : '{} - {}'.format(article['title'], self.site.translate(language, name))
        }

        if os.path.exists(full_src_path):

            obj = {
                'type' : 'md',
                'bare' : True,
                'h-offset' : 2,
            }

            src = self.site.load('file://{}'.format(src_path))
            parsed_markdown = self.site.process(src, obj, vars, language)
            #we do another Jinja pass (to parse links etc.)
            vars['{}_content'.format(name)] = self.site.process(parsed_markdown, {'type': 'html'}, vars, language)
        input = self.site.load(law['templates'][name])
        output = self.site.process(input, {'type' : 'html', 'name' : article['{}_name'.format(name)]}, vars, language)
        filename = self.site.get_dst(article['{}_slug'.format(name)], language)
        self.site.write(output, filename)
