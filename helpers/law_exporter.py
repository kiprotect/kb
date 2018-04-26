import os
import yaml

#https://stackoverflow.com/questions/8640959/how-can-i-control-what-scalar-form-pyyaml-uses-for-my-data

def str_presenter(dumper, data):
    if len(data) > 100:
        return dumper.represent_scalar(u'tag:yaml.org,2002:str', data, style='|')
    else:
        return dumper.represent_scalar(u'tag:yaml.org,2002:str', data, style=None)

yaml.add_representer(str, str_presenter)

def update(d, ud, overwrite=True):
    for key, value in ud.items():
        if key not in d:
            d[key] = value
        elif isinstance(value, dict):
            update(d[key], value, overwrite=overwrite)
        elif isinstance(value, list) and isinstance(d[key], list):
            d[key] = value
        else:
            if key in d and not overwrite:
                return
            d[key] = value

def write_yaml(filename, data, merge=True):
    if merge:
        if os.path.exists(filename):
            with open(filename) as input_file:
                old_data = yaml.load(input_file.read())
            if old_data is not None:
                update(old_data, data)
            else:
                old_data = data
            data = old_data
    with open(filename, 'w') as output_file:
        output_file.write(yaml.dump(data, default_flow_style=False))

def store_result(result, build_dir):
    all_file = os.path.join(build_dir, 'all.yml')
    os.makedirs(build_dir, exist_ok=True)
    write_yaml(all_file, result)
    recitals_dir = os.path.join(build_dir, 'recitals')
    footnotes_dir = os.path.join(build_dir, 'footnotes')
    os.makedirs(recitals_dir, exist_ok=True)

    main = {
        'chapters' : [],
        'footnotes' : [],
        'recitals' : [],
    }
    for recital_key, recital in result['recitals'].items():
        recital_file = os.path.join(recitals_dir, '{}.yml'.format(recital_key))
        main['recitals'].append({'$include' : os.path.relpath(recital_file, build_dir)})
        write_yaml(recital_file, recital)
    os.makedirs(footnotes_dir, exist_ok=True)
    for footnote_key, footnote in result['footnotes'].items():
        footnote_file = os.path.join(footnotes_dir, '{}.yml'.format(footnote_key))
        main['footnotes'].append({'$include' : os.path.relpath(footnote_file, build_dir)})
        write_yaml(footnote_file, footnote)
    for chapter_key, chapter in result['chapters'].items():
        chapter_dir = os.path.join(build_dir, 'chapters/{}'.format(chapter_key))
        sections = chapter['sections']
        chapter['sections'] = []
        for section_key, section in sections.items():
            section_dir = os.path.join(chapter_dir,'sections/{}'.format(section_key))
            section['chapter'] = chapter_key
            articles_dir = os.path.join(section_dir, 'articles')
            os.makedirs(articles_dir, exist_ok=True)
            articles = section['articles']
            section['articles'] = []
            for article_key, article in articles.items():
                article_file = os.path.join(articles_dir, '{}.yml'.format(article_key))
                article['chapter'] = chapter_key
                article['section'] = section_key
                write_yaml(article_file, article)
                section['articles'].append({'$include' : os.path.relpath(article_file, section_dir)})
            section_file = os.path.join(section_dir,'main.yml')
            write_yaml(section_file, section)
            chapter['sections'].append({'$include' : os.path.relpath(section_file, chapter_dir)})
        chapter_file = os.path.join(chapter_dir,'main.yml')
        write_yaml(chapter_file, chapter)
        main['chapters'].append({'$include' : os.path.relpath(chapter_file, build_dir)})
    write_yaml(os.path.join(build_dir,'main.yml'), main)
