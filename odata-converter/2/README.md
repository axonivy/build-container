Converter OData 2 to OpenAPI 3
==============================

Converting an OData 2 to OpenAPI 3 file with this container.
You will need to make the OData definition available in the
container and refer.

    docker run -v $(pwd):/tmp/work axonivy/build-container:odata-converter-2 -p /tmp/work/source.xml


## Reference

https://github.com/oasis-tcs/odata-openapi/tree/master/tools#transformjs-for-nodejs
