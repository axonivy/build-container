def build(def directory) {
  def tag = directory.replace("/", "-")
  def name = "axonivy/build-container:${tag}"
  echo "Building container tag $tag in directory $directory"
  dir (directory) {    
    def image = docker.build(name)
    if (env.BRANCH_NAME == 'master') {
      docker.withRegistry('', 'docker.io') {
        image.push()
      }
    }
    sh "docker image rm ${name}"
  }
}
