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

def eval_version():
    # 1. get version from environment variable
    import os
    if "VERSION" in os.environ:
      return os.environ['VERSION']

    # 2. get version from pom.xml <VERSION>
    pomVersion = parse_version_from_pom()
    if pomVersion is not None:
      release = pomVersion.removesuffix('-SNAPSHOT').rsplit('.',1)[0]
      return release

    # 3. fallback to dev version
    return 'dev'

def parse_version_from_pom():
    import os
    pomFile = os.environ['BASEDIR'] + '/pom.xml'
    if os.path.isfile(pomFile):
      from xml.etree import ElementTree as et
      tree = et.ElementTree()
      tree.parse(pomFile)
      ns = {"mvn":"http://maven.apache.org/POM/4.0.0"}
      version = tree.getroot().find('./mvn:version', ns)
      if version is not None:
        return version.text
      parentVersion = tree.getroot().find('./mvn:parent/mvn:version', ns)
      if parentVersion is not None:
        return parentVersion.text
    return None

def parse_project_name_from_pom():
    import os

    if "PROJECT_NAME" in os.environ:
      return os.environ['PROJECT_NAME']

    from xml.etree import ElementTree as et
    tree = et.ElementTree()
    tree.parse(os.environ['BASEDIR'] + '/pom.xml')
    ns = {"mvn":"http://maven.apache.org/POM/4.0.0"}
    name = tree.getroot().find('./mvn:name', ns).text
    return name

def localeDir():
    # 1. get from environment variable
    import os
    if "LOCALEDIR" in os.environ:
      return os.environ['LOCALEDIR']

    # 2. fallback best practice
    return 'locales/'

def language():
    # 1. get from environment variable
    import os
    if "SPHINXOPTS" in os.environ:
      opts = os.environ['SPHINXOPTS']
      lang =  opts.split("language='")[1]
      lang = lang.split("'")[0]
      return lang

    # 2. fallback best practice
    return 'en'

def versionSwitcher():
  import os
  return "VERSION_SWITCHER" in os.environ

def gettextCompact():
    # 1. get from environment variable
    import os
    if "GETTEXT_COMPACT" in os.environ:
      return os.environ['GETTEXT_COMPACT']

    # 2. fallback best practice
    return True

# project
project = parse_project_name_from_pom()
copyright = get_current_year() + ' Axon Ivy AG'
version = eval_version()
buildExampleVersion = parse_build_example_version()
branchVersion = parse_branch_version()
release = version
language = language()

import sys
sys.stdout.write("version: " +version+"\n")
sys.stdout.write("version_branch: " +branchVersion+"\n")

# general options
needs_sphinx = '8.0'
master_doc = 'index'
pygments_style = 'tango'
add_function_parentheses = True

if versionSwitcher():
  templates_path = ['_templates']

html_context = {
  'current_project' : project,
  'current_version' : version,
  'current_language': language,
}

# graphviz
graphviz_output_format = 'svg'
graphviz_dot_args = [
  # node
  '-Nfontsize=15',
  '-Nfontname=Roboto,Helvetica Neue,Arial,sans-serif',
  '-Nfontcolor=#FFFFFF',
  '-Ncolor=#007095',
  '-Nshape=box',
  '-Nstyle=filled',
  '-Nheight=0.8',
  '-Nfixedsize=true',
  '-Nwidth=2',
  # edge
  '-Efontsize=15',
  '-Efontname=Roboto,Helvetica Neue,Arial,sans-serif'
]


import sphinx_rtd_theme
extensions = [
  'sphinx.ext.extlinks',
  'sphinx.ext.graphviz',
  'sphinxcontrib.httpdomain',
  'sphinx_rtd_theme',
  'myst_parser',
  'sphinx_design'
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

# locales
locale_dirs = [localeDir()]
gettext_compact = gettextCompact()

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
