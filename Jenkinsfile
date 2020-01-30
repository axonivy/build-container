images = ['all', 'rcptt/1.1', 'read-the-docs/1.2', 'ssh-client/1.0', 'web/1.0', 'eclipse-test/1.0', 'oracle']

pipeline {
  agent any

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
          if (image == 'all') {
            images.each {
              runBuild(it);              
            }
          } else {
            runBuild(image)
          }
        }
      }
    }

  }
}

def runBuild(def image) {
  if (image == 'oracle') {
    buildOracleDb()
  } else if (image == 'all') {
    return
  } else {
     build(image)              
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


def buildOracleDb() {
  sh 'rm -rf docker-images'
  sh 'git clone https://github.com/oracle/docker-images'

  buildOracleImage('http://zugpronas:5000/fbsharing/MJy3pk5S', '12.2.0.1', 'linuxx64_12201_database.zip', 'oracle/database:12.2.0.1-se2')
  buildOracleImage('http://zugpronas:5000/fbsharing/5JgTn1Co', '19.3.0', 'LINUX.X64_193000_db_home.zip', 'oracle/database:19.3.0-se2')
}

def buildOracleImage(String oracleBinaryUrl, String version, String filename, def image) {
  dir ('docker-images/OracleDatabase/SingleInstance/dockerfiles') {
    // download oracle binary
    sh "curl -L $oracleBinaryUrl -o $version/$filename"

    // -v = Version, -s = Standard Edition
    sh "./buildDockerImage.sh -v $version -s"

    docker.withRegistry('https://registry.ivyteam.io', 'registry.ivyteam.io') {
      docker.image(image).push()
    }
  }
}
