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
            docker.withRegistry('', 'docker.io') {
              docker.build("axonivy/build-container:rcptt-1.1").push()
            }
          }

        }
      }
    }

  }
}
