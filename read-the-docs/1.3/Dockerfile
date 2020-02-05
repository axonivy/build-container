FROM python:3.7-alpine

ADD requirements.txt requirements.txt

RUN apk add --update --no-cache make && \
    pip3 install -r requirements.txt

ARG RTD_THEME_DIR=/usr/local/lib/python3.7/site-packages/sphinx_rtd_theme

# customize theme with custom.css
ADD custom.css /tmp
RUN cat /tmp/custom.css >> $RTD_THEME_DIR/static/css/theme.css

# remove not needed fonts
RUN rm $RTD_THEME_DIR/static/fonts/Inconsolata* && \
    rm -rf $RTD_THEME_DIR/static/fonts/Lato && \
    rm -rf $RTD_THEME_DIR/static/fonts/RobotoSlab && \
    rm $RTD_THEME_DIR/static/fonts/Lato* && \
    rm $RTD_THEME_DIR/static/fonts/RobotoSlab*

# add sphix build files
ADD Makefile conf.py /doc-build/

# add images
ADD axonivylogo.svg favicon.png /doc-build/images/

# removed modernizers, which triggers page reflows (flickering loading)
# made changes to get rid of sphinx warning see here:
# https://github.com/readthedocs/sphinx_rtd_theme/commit/a49a812c8821123091166fae1897d702cdc2d627#diff-b3d4a9c32d5abd89b9214dcfbb2ece79
RUN rm $RTD_THEME_DIR/static/js/modernizr.min.js
ADD search.html layout.html $RTD_THEME_DIR/

# for build environment
RUN chown -R 1000:1000 /doc-build
USER 1000:1000

WORKDIR /doc-build
