# read-the-docs

Building your rst files with read the docs.

## preview

Use it as previewer with `docker-compose`:

The container needs to have to all sphinx
ressources (`.rst` files, images, code-snippets, etc.)
available.

So you need to provide this as volume into the container somewhere.
And define `BASEDIR` as parameter where this place is in the container.

    version: '3.3'
    services:
    builder:
        image: axonivy/build-container:read-the-docs-1.1
        ports:
        - "8000:8000"
        volumes:
        - "./..:/ivy-core"     
        entrypoint: "make livehtml BASEDIR=/ivy-core/doc"


## build pipeline

You can use this container as build container within your `Jenkinsfile`.
Jenkins provides automatically all data into the build container, you have to define with `BASEDIR` where Jenkins will provide that.

Additionally we `enableAllExtensions`. There are some extensions
which are not relay needed for preview and makes the build slow.

    docker.image('axonivy/build-container:read-the-docs-1.1').inside {
        sh "make -C /doc-build SPHINXOPTS='-t enableAllExtensions' html BASEDIR='${env.WORKSPACE}/doc'"
    }
