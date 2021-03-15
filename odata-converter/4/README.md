Converter OData 4 to OpenAPI 3
==============================

Converting an OData 4 to OpenAPI3 file with this container.
You will need to make the OData definition available in the
container and refer.

    docker run -v $(pwd):/tmp/work axonivy/build-container:odata-converter-4 -p /tmp/work/source.xml
