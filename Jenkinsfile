pipeline {
  agent {
    label 'docker'
  }

  options {
    buildDiscarder(logRotator(artifactNumToKeepStr: '50'))
  }

  triggers {
    pollSCM 'H/10 * * * *'
    cron '@midnight'
  }

  stages {

    stage('build') {
      steps {
        script {
          build('rcptt/1.1', 'rcptt-1.1')
          build('read-the-docs/1.0', 'read-the-docs-0.0')
        }
      }
    }

  }
}

def build(def directory, def tag) {
  dir (directory) {
    docker.withRegistry('', 'docker.io') {
      docker.build("axonivy/build-container:${tag}").push()
    }
  }
}
