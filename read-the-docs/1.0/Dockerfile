FROM python:alpine

ADD requirements.txt requirements.txt

RUN apk add --update --no-cache make && \
    pip3 install -r requirements.txt

ADD Makefile /doc-build/
WORKDIR /doc-build

RUN chown 1000:1000 /doc-build

USER 1000:1000
