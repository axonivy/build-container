# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
BASEDIR       = .
SOURCEDIR     = $(BASEDIR)/source
BUILDDIR      = $(BASEDIR)/build
CONFIGDIR     = /doc-build

# this environment variable will be read by conf.py
export BASEDIR=$(BASEDIR)

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -b help -c "$(CONFIGDIR)" "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# auto build documentation on file change and provide web browser "make livehtml"
livehtml:
	sphinx-autobuild -c "$(CONFIGDIR)" --host 0.0.0.0 "$(SOURCEDIR)" "$(BUILDDIR)/html" $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -b $@ -c "$(CONFIGDIR)" "$(SOURCEDIR)" "$(BUILDDIR)/$@" $(SPHINXOPTS) $(O)
