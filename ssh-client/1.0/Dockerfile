FROM alpine:3

RUN apk update \
 && apk upgrade \
 && apk add --no-cache \
            rsync \
            openssh-client \
            ca-certificates \
 && update-ca-certificates \
 && rm -rf /var/cache/apk/*

RUN addgroup -g 1000 build && adduser -u 1000 -G build -D -g "" build && \
    mkdir -p /home/build/.ssh && \
    echo -e "Host *\n   StrictHostKeyChecking no" > /home/build/.ssh/config && \
    chown -R build /home/build/.ssh
