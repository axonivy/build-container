FROM alpine:3

RUN apk update \
 && apk upgrade \
 && apk add --no-cache \
            wget \
            unzip \
 && rm -rf /var/cache/apk/*
