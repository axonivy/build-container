# -*- coding: utf-8 -*-

def get_current_year():
    from datetime import datetime
    return str(datetime.today().year)

def parse_version_from_pom():
    import os
    from xml.etree import ElementTree as et
    tree = et.ElementTree()    
    tree.parse(os.environ['BASEDIR'] + '/pom.xml')
    ns = {"mvn":"http://maven.apache.org/POM/4.0.0"}
    version = tree.getroot().find('./mvn:parent/mvn:version', ns).text
    if version.endswith('-SNAPSHOT'):
        version = version[:-9]
    return version

# project
project = 'Axon.ivy Digital Business Platform'
copyright = get_current_year() + ', AXON Ivy AG'
version = parse_version_from_pom()
release = version

# general options
needs_sphinx = '1.5.6'
master_doc = 'index'
pygments_style = 'tango'
add_function_parentheses = True

extensions = [
  'sphinx.ext.extlinks',    
  'sphinxcontrib.httpdomain'
]
exclude_trees = []
source_suffix = ['.rst']
source_encoding = 'utf-8-sig'
exclude_patterns = ['**/_*.rst'] # all rst files starting with _ do we use as includes

# html options
html_theme = 'sphinx_rtd_theme'
html_use_index = True
html_show_sourcelink = False
html_logo = '/doc-build/images/axonivylogo.svg'
html_theme_options = {
    'logo_only': True
}
html_show_sphinx = False
html_favicon = '/doc-build/images/favicon.png'

# base urls
# https://stackoverflow.com/questions/1227037/substitutions-inside-links-in-rest-sphinx
extlinks = {
    'dev-url':  ('https://developer.axonivy.com%s', None),
    'public-api':  ('https://developer.axonivy.com/doc/latest/public-api%s', None),
    'java-api':  ('https://docs.oracle.com/en/java/javase/11/docs/api%s', None),
}

# token replacements
# https://github.com/sphinx-doc/sphinx/issues/4054
replacements = {
    '|ivy-platform|': 'Axon.ivy Digital Business Platform',
    '|ivy-engine|' : 'Axon.ivy Engine',
    '|ivy-designer|': 'Axon.ivy Designer',
    '|axon-ivy|': 'Axon.ivy',
}

def replace_token(app, docname, source):
    result = source[0]
    for key in app.config.replacements:
        result = result.replace(key, app.config.replacements[key])
    source[0] = result

def setup(app):
    app.add_config_value('replacements', {}, True)
    app.connect('source-read', replace_token)
