FROM selenium/node-base

RUN sudo apt-get -qqy update && sudo apt-get -qqy install openjdk-11-jdk-headless maven libswt-gtk-4-java

RUN sudo sed -i -e '/^assistive_technologies=/s/^/#/' /etc/java-*-openjdk/accessibility.properties
