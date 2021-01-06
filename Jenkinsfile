images = ['all', 'rcptt/1.2', 'read-the-docs/2', 'ssh-client/1.0', 'web/1.0', 'eclipse-test/1.0', 'oracle', 'edirectory']

pipeline {
  agent any

  options {
    buildDiscarder(logRotator(artifactNumToKeepStr: '50'))
  }
  
  parameters {
    choice name: 'image', choices: images
  }

  triggers {
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
  } else if (image == 'edirectory'){
    buildEdirectory()
  } else {
    docker.withRegistry('', 'docker.io') {
      build(image)
    }
  }
}

def buildEdirectory(){
  sh 'wget http://zugpronas:5000/fbsharing/ofPMJOCK -O /tmp/edirectory.tar.gz'
  sh 'tar -xvf /tmp/edirectory.tar.gz -C /tmp'
  sh 'docker load --input /tmp/edir920.tar'
  def image = docker.image("edirectory:9.2.0")
  docker.withRegistry('https://docker-registry.ivyteam.io', 'docker-registry.ivyteam.io') {
    if (env.BRANCH_NAME == 'master') {
      image.push()
    }
  }
}

def build(def directory) {
  def tag = directory.replace("/", "-")
  echo "Building container tag $tag in directory $directory"
  dir (directory) {
    docker.withRegistry('', 'docker.io') {
      def image = docker.build("axonivy/build-container:${tag}")
      if (env.BRANCH_NAME == 'master') {
        image.push()
      }
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
  def baseImage
  dir ('docker-images/OracleDatabase/SingleInstance/dockerfiles') {
    // download oracle binary
    sh "curl -L $oracleBinaryUrl -o $version/$filename"

    // -v = Version, -s = Standard Edition
    sh "./buildDockerImage.sh -v $version -s"

    baseImage = docker.image(image)
    docker.withRegistry('https://docker-registry.ivyteam.io', 'docker-registry.ivyteam.io') {
      if (env.BRANCH_NAME == 'master') {
        baseImage.push()
      }
    }
  }
  def currentDir = pwd()
  sh "mkdir oracle/${version}/data"
  sh "chmod 777 oracle/${version}/data"
  
  baseImage.withRun("-v ${currentDir}/oracle/${version}/data:/opt/oracle/oradata -v ${currentDir}/oracle/${version}/dbca.rsp.tmpl:/opt/oracle/dbca.rsp.tmpl --user=54321:1000 "+'-e "ORACLE_SID=ORASID" -e "ORACLE_PDB=ORAPDB" -e "ORACLE_CHARACTERSET=AL32UTF8" -e "ORACLE_PWD=nimda"') { container -> 
    waitUntilDbIsReady(container)
  }
  
  def dbImage = docker.build("oracle/database-orapdb:${version}-se2", "oracle/${version}")
  docker.withRegistry('https://docker-registry.ivyteam.io', 'docker-registry.ivyteam.io') {
    if (env.BRANCH_NAME == 'master') {
      dbImage.push()
    }
  }

  makeDataDirDeleteableForJenkins(dbImage, currentDir, version)
}

def waitUntilDbIsReady(container)
{
  def attempts = 0;
  while (attempts < 180) 
  {
    if (isDbReady(container))
    {
      return
    }
    attempts++
    sleep 10
  }
  error("Database initialization timeouted after 30 minutes")
}

def isDbReady(container)
{
  return sh (script: "docker logs ${container.id} | grep 'DATABASE IS READY TO USE!'", returnStatus: true) == 0
}

def makeDataDirDeleteableForJenkins(dbImage, currentDir, version)
{
  dbImage.withRun(" -v ${currentDir}/oracle/${version}/data:/opt/oracle/oradata --user=54321:1000", "chmod -R 777 /opt/oracle/oradata/ORASID", { container -> })
  dbImage.withRun(" -v ${currentDir}/oracle/${version}/data:/opt/oracle/oradata --user=54321:1000", "chmod -R 777 /opt/oracle/oradata/dbconfig", { container -> })
}
