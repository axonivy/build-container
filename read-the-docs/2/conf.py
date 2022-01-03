# -*- coding: utf-8 -*-

def get_current_year():
    from datetime import datetime
    return str(datetime.today().year)

# only needed for 9.2 and earlier branches - can be deleted once we drop support or when we change to link-url in these branches as well
def parse_build_example_version():

    # 1. get version from environment variable
    import os
    if "BUILD_EXAMPLE_VERSION" in os.environ:
      return os.environ['BUILD_EXAMPLE_VERSION']
    return 'master'

def parse_branch_version():
    import os
    if "BRANCH_VERSION" in os.environ:
      return os.environ['BRANCH_VERSION']
    return 'master'

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

def parse_major_version(version):
    major = version.split(".")[0]
    if major.isnumeric():
        return major
    return version

# project
project = parse_project_name_from_pom()
copyright = get_current_year() + ' Axon Ivy AG'
version = parse_version_from_pom()
buildExampleVersion = parse_build_example_version()
branchVersion = parse_branch_version()
release = version

# general options
needs_sphinx = '3.3'
master_doc = 'index'
pygments_style = 'tango'
add_function_parentheses = True

# graphviz
graphviz_output_format = 'png'
graphviz_dot_args = [
  # node
  '-Nfontsize=15',
  '-Nfontname=NotoSans',
  '-Nfontcolor=#FFFFFF',
  '-Ncolor=#007095',
  '-Nshape=box',
  '-Nstyle=filled',
  '-Nheight=0.8',
  '-Nfixedsize=true',
  '-Nwidth=2',
  # edge
  '-Efontsize=15',
  '-Efontname=NotoSans'
]


import sphinx_rtd_theme
extensions = [
  'sphinx.ext.extlinks',
  'sphinx.ext.graphviz',
  'sphinxcontrib.httpdomain',
  'sphinx_rtd_theme',
  'm2r2'
]
exclude_trees = []
source_suffix = ['.rst', '.md']
source_encoding = 'utf-8-sig'
exclude_patterns = ['**/_*.rst', '**/_*.md'] # all rst files starting with _ do we use as includes

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
    'dev-url': ('https://developer.axonivy.com%s', None),
    'public-api': ('https://developer.axonivy.com/doc/' + version + '/public-api%s', None),
    'java-api': ('https://docs.oracle.com/en/java/javase/11/docs/api%s', None),
    'portal-url': ('https://developer.axonivy.com/portal/' + version + '/doc%s', None),
    # only needed for 9.2 and earlier branches - can be deleted once we drop support or when we change to link-url in these branches as well
    'github-build-examples': ('https://github.com/axonivy/project-build-examples/blob/' + buildExampleVersion + '/compile-test%s', None),
    'api-browser-url': ('https://developer.axonivy.com/api-browser?configUrl=https://developer.axonivy.com/doc/' + version + '/openapi/config.json&urls.primaryName=%s', None),
    'project-build-plugin-doc': ('https://axonivy.github.io/project-build-plugin/release/%s', None),
    'link-url': ('https://developer.axonivy.com/link/%s/' + branchVersion, None),
}

# token replacements
# https://github.com/sphinx-doc/sphinx/issues/4054
replacements = {
    '|ivy-platform|': 'Axon Ivy Platform',
    '|ivy-engine|' : 'Axon Ivy Engine',
    '|ivy-designer|': 'Axon Ivy Designer',
    '|axon-ivy|': 'Axon Ivy',
    '|version|': version,
    '|majorVersion|': parse_major_version(version),
}

rst_epilog = """
.. |tag-ops-wizard| image:: https://img.shields.io/badge/Operations-Wizard-green.svg
.. |tag-ops-changed| image:: https://img.shields.io/badge/Operations-Changed-yellow.svg
.. |tag-ops-deprecated| image:: https://img.shields.io/badge/Operations-Deprecated-orange.svg
.. |tag-ops-removed| image:: https://img.shields.io/badge/Operations-Removed-red.svg
.. |tag-project-auto-convert| image:: https://img.shields.io/badge/Project-AutoConvert-green.svg
.. |tag-project-changed| image:: https://img.shields.io/badge/Project-Changed-yellow.svg
.. |tag-project-deprecated| image:: https://img.shields.io/badge/Project-Deprecated-orange.svg
.. |tag-project-removed| image:: https://img.shields.io/badge/Project-Removed-red.svg
"""

def replace_token(app, docname, source):
    result = source[0]
    for key in app.config.replacements:
        result = result.replace(key, app.config.replacements[key])
    source[0] = result

def setup(app):
    app.add_config_value('replacements', {}, True)
    app.connect('source-read', replace_token)
