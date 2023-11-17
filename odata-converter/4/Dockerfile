# https://github.com/oasis-tcs/odata-openapi/tree/master/lib
FROM node:20-buster

RUN git clone https://github.com/oasis-tcs/odata-openapi odata-openapi && \
    cd odata-openapi && \
    npm install

ENTRYPOINT [ "odata-openapi/lib/cli.js" ]
