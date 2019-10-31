FROM alpine:3.10

RUN apk update \
 && apk upgrade \
 && apk add --no-cache \
            rsync \
            openssh-client \
            ca-certificates \
 && update-ca-certificates \
 && rm -rf /var/cache/apk/* \
 && echo "Host *\n   StrictHostKeyChecking no" > /etc/ssh/ssh_config
