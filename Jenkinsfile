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
          dir ('rcptt') {
            docker.build("build-container:rcptt-1.0")
          }
        }
      }
    }

  }
}
