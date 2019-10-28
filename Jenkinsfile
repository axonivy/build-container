images = ['all', 'rcptt/1.1', 'read-the-docs/1.2']

pipeline {
  agent {
    label 'docker'
  }

  options {
    buildDiscarder(logRotator(artifactNumToKeepStr: '50'))
  }
  
  parameters {
    choice name: 'image', choices: images
  }

  triggers {
    pollSCM 'H/10 * * * *'
    cron '@midnight'
  }

  stages {

    stage('build') {
      steps {
        script {
          def image = params.image;
          if (image?.trim() || image == 'all') {
            images.each {
              if (it != 'all') {
                build(it)
              }
            }
          } else {
            build(image)
          }
        }
      }
    }

  }
}

def build(def directory) {
  def tag = directory.replace("/", "-")
  echo "Building container tag $tag in directory $directory"
  dir (directory) {
    docker.withRegistry('', 'docker.io') {
      docker.build("axonivy/build-container:${tag}").push()
    }
  }
}
