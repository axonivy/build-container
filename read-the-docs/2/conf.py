# -*- coding: utf-8 -*-

def get_current_year():
    from datetime import datetime
    return str(datetime.today().year)

def parse_version_from_pom():

    # 1. get version from environment variable
    import os
    if "VERSION" in os.environ:
      return os.environ['VERSION']

    # 2. get version from pom.xml <VERSION>    
    pomFile = os.environ['BASEDIR'] + '/pom.xml'
    if os.path.isfile(pomFile):
      from xml.etree import ElementTree as et
      tree = et.ElementTree()
      tree.parse(pomFile)
      ns = {"mvn":"http://maven.apache.org/POM/4.0.0"}
      element = tree.getroot().find('./mvn:version', ns)
      if element is not None:
        return element.text      

    # 3. fallback to dev version
    return 'dev'

def parse_project_name_from_pom():
    import os
    from xml.etree import ElementTree as et
    tree = et.ElementTree()    
    tree.parse(os.environ['BASEDIR'] + '/pom.xml')
    ns = {"mvn":"http://maven.apache.org/POM/4.0.0"}
    name = tree.getroot().find('./mvn:name', ns).text
    return name

# project
project = parse_project_name_from_pom()
copyright = get_current_year() + ' AXON Ivy AG'
version = parse_version_from_pom()
release = version

# general options
needs_sphinx = '3.1'
master_doc = 'index'
pygments_style = 'tango'
add_function_parentheses = True
graphviz_output_format = 'png'

extensions = [
  'sphinx.ext.extlinks',
  'sphinx.ext.graphviz',
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
html_css_files = [
    'custom.css'
]
html_js_files = [
    'https://cdnjs.cloudflare.com/ajax/libs/jQuery-linkify/2.1.9/linkify.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/jQuery-linkify/2.1.9/linkify-jquery.min.js',
    'custom.js'
]
html_show_sphinx = False
html_favicon = '/doc-build/images/favicon.png'

# base urls
# https://stackoverflow.com/questions/1227037/substitutions-inside-links-in-rest-sphinx
extlinks = {
    'dev-url':  ('https://developer.axonivy.com%s', None),
    'public-api':  ('https://developer.axonivy.com/doc/' + version + '/public-api%s', None),
    'java-api':  ('https://docs.oracle.com/en/java/javase/11/docs/api%s', None),
    'portal-url':  ('https://developer.axonivy.com/portal/' + version + '/doc%s', None),
    'github-build-examples': ('https://github.com/axonivy/project-build-examples/blob/master/compile-test%s', None),
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
