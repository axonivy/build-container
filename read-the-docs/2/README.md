# read-the-docs

Building your rst files with read the docs.

You need a `pom.xml` in your root folder
which defines a `<name>` xml tag.
This will be used as project title.

## preview

Use it as previewer with `docker-compose`:

The container needs to have access to all sphinx
ressources (`.rst` files, images, code-snippets, etc.)
available.

So you need to provide this as volume into the container somewhere.
And define `BASEDIR` as parameter where this place is in the container.

    services:
      builder:
        image: axonivy/build-container:read-the-docs-2
        ports:
        - 8000:8000
        volumes:
        - ./..:/ivy-core
        entrypoint: make livehtml BASEDIR=/ivy-core/doc


## build pipeline

You can use this container as build container within your `Jenkinsfile`.
Jenkins provides automatically all data into the build container, you have to define with `BASEDIR` where Jenkins will provide that.
Furthermore you need to define the `VERSION`.

    docker.image('axonivy/build-container:read-the-docs-2').inside {
        sh "make -C /doc-build html BASEDIR='${env.WORKSPACE}/doc' VERSION=${env.BRANCH_NAME}"
    }

# version switcher

The version switcher can be enabled by defining `VERSION_SWITCHER=true`.

Current versions and languages are loaded from a REST endpoint that must be located at the path `/api/docs/{product}/{version}/{language}` 
on the website that hosts the documentation. The response must have the following format:

```json
{
    "versions":[
        {"version":"10.0","url":"https:\/\/dev.axonivy.com\/doc\/10.0\/en"},
        {"version":"12.0","url":"https:\/\/dev.axonivy.com\/doc\/12.0\/en"},
        {"version":"13.2","url":"https:\/\/dev.axonivy.com\/doc\/13.2\/en"},
    "languages":[
        {"language":"en","url":"https:\/\/dev.axonivy.com\/doc\/13.2\/en"},
        {"language":"ja","url":"https:\/\/dev.axonivy.com\/doc\/13.2\/ja"}]
}
```

# translations

The usage in the core repository looks as follow:

```bash
cd ~/git/core/doc
```

## step 1: generate pot files

```bash
docker run -v ./../:/ivy-core axonivy/build-container:read-the-docs-2 make gettext BASEDIR=/ivy-core/doc
ll build/gettext
```

## step 2: generate/update po files (per language)

```bash
docker run -v ./../:/ivy-core axonivy/build-container:read-the-docs-2 make generatePO BASEDIR=/ivy-core/doc LOCALEDIR=/ivy-core/doc/build/locale LANGUAGE=de,ja,fr
ll build/po
```

## step 3: translate these po files in folder build/po

- If something changes in the POT files (from step 1), then you can run step 2
- Translators can update the PO files from step 2 any time they want

## step 4: generate doc per language

```bash
docker run -v ./../:/ivy-core axonivy/build-container:read-the-docs-2 make html BASEDIR=/ivy-core/doc LOCALEDIR=/ivy-core/doc/build/locale SPHINXOPTS="-D language='ja'"
```
