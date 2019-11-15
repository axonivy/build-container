FROM selenium/standalone-firefox:3.141.59

RUN sudo apt-get -qqy update && sudo apt-get -qqy install openjdk-11-jdk maven libswt-gtk-4-java libwebkitgtk-3.0-0 libwebkit2gtk-4.0-37 openjfx

USER root
COPY docker-entrypoint.sh /opt/docker-entrypoint.sh
RUN chmod +x /opt/docker-entrypoint.sh

USER seluser
ENTRYPOINT ["/opt/docker-entrypoint.sh"]
