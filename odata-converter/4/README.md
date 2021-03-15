Converter OData 4 to OpenAPI 3
==============================

Converting an OData 3 and 4 to OpenAPI 3 schema with this container.
You will need to make the OData definition available in the
container and refer to it. The OpenAPI spec will be written
to the current directory.


    docker run -v $(pwd):/tmp/work axonivy/build-container:odata-converter-4 -p /tmp/work/source.xml
