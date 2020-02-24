pipeline {
   pipeline {
    agent {
    // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
    dockerfile {
        filename 'Dockerfile.build'
        dir 'build'
        label 'my-defined-label'
        additionalBuildArgs  '--build-arg version=1.0.2'
        }
    }
    stages {
       stage('Build') {
            steps {
              echo '编译'
              sleep 10
            }
        }
        stage('Deploy') {
            steps {
               echo 'Deploying....'
            }
        }
    }
}
