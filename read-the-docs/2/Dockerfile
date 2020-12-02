FROM python:3.8-alpine

ADD requirements.txt requirements.txt

RUN apk add --update --no-cache make && \
    apk add --update --no-cache graphviz ttf-ubuntu-font-family && \
    pip3 install -r requirements.txt

# add custom css and javascript to the theme
ARG RTD_THEME_DIR=/usr/local/lib/python3.8/site-packages/sphinx_rtd_theme
ADD custom.css $RTD_THEME_DIR/static/custom.css
ADD custom.js $RTD_THEME_DIR/static/custom.js

# add sphinx build files
ADD Makefile conf.py /doc-build/

# add images
ADD axonivylogo.svg favicon.png /doc-build/images/

# for build environment
RUN chown -R 1000:1000 /doc-build
USER 1000:1000

WORKDIR /doc-build
