FROM selenium/node-base

RUN sudo apt-get -qqy update && sudo apt-get -qqy install openjdk-11-jdk-headless maven libswt-gtk-4-java

RUN sudo sed -i -e '/^assistive_technologies=/s/^/#/' /etc/java-*-openjdk/accessibility.properties

USER root
COPY docker-entrypoint.sh /opt/docker-entrypoint.sh
RUN chmod +x /opt/docker-entrypoint.sh

# add an user with 1000 for the build in jenkins
RUN addgroup --gid 1000 build && adduser --uid 1000 --gid 1000 --disabled-password --gecos "" build

USER seluser
ENTRYPOINT ["/opt/docker-entrypoint.sh"]
