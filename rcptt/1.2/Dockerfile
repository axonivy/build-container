FROM selenium/node-base

RUN wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | sudo apt-key add - > /dev/null 2>&1 && \
    sudo apt-get -qqy update && sudo apt-get -qqy install software-properties-common && \
    sudo add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/ && \
    sudo apt-get -qqy install adoptopenjdk-11-hotspot maven libswt-gtk-4-java libwebkitgtk-3.0-0 libwebkit2gtk-4.0-37 openjfx

USER root
COPY docker-entrypoint.sh /opt/docker-entrypoint.sh
RUN chmod +x /opt/docker-entrypoint.sh

USER seluser
ENTRYPOINT ["/opt/docker-entrypoint.sh"]
