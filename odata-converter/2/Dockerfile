FROM node:17-stretch

RUN echo "deb http://archive.debian.org/debian stretch stretch-security main contrib non-free" > /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/oasis-tcs/odata-openapi odata-openapi && \
    cd odata-openapi/tools && \
    npm install

RUN npm install -g node-gyp

ENTRYPOINT [ "node", "odata-openapi/tools/transform.js" ]
