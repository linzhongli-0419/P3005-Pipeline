pipeline {
  agent any
  environment {
    BUILD = sh (script: 'git rev-list HEAD --count', returnStdout: true).trim()
    GIT_COMMIT = sh (script: 'git rev-parse HEAD', returnStdout: true).trim()

    SERVER_HOST = '119.23.130.213'
    SERVER_SSH_PORT = 8022
    SERVER_USER = "ones-api"
    DEST_DIR = "${WORKSPACE}/dest"

    PROJECT_ROOT = "/data/app/project-api"
    LOG_ROOT = "/data/log/app/project"
    OP_DIR = "/data/app/project-api/dest"
    PROJECT_DIR="${PROJECT_ROOT}/${BRANCH_NAME}"
    LOG_DIR="${LOG_ROOT}/${BRANCH_NAME}"
    TAR_FILE_NAME = "${BRANCH_NAME}.tar.gz"

    ENABLE_POST_FUNC = "true" //开启后置动作

    WIKI_DB_NAME =  ("wiki_" + env.BRANCH_NAME).trim().toLowerCase()
    PROJECT_DB_NAME =  ("project_" + env.BRANCH_NAME).trim().toLowerCase()
  }

  stages {
    stage('参数检查') {
      steps {
        script {
          if (env.BRANCH_NAME == "Newmaster2"){
          sh "ps -a"
         }
        }
      }
    }
<<<<<<< HEAD
=======
  
>>>>>>> ffe763bcb19cdc0cc8f2d2b33f904209b71b5a55
    stage('编译,打包') {
       steps {
          echo 'Build runing......'
          sh "ps -a"
         }
      }
    stage('编译,打包') {
       steps {
          echo 'Build runing......'
          sh "ps -ef"
         }
      }
    stage('编译,打包') {
       steps {
          echo 'Build runing......'
          sh "ps -a"
         }
      }
    }
  post {
    always {
      echo 'Pipeline finished, Pushing notification now ...'
    }
    success {
      sh 'pwd'
    }
    unsuccessful {
      sh 'pwd'
    }
  }
<<<<<<< HEAD
}
=======

}
>>>>>>> ffe763bcb19cdc0cc8f2d2b33f904209b71b5a55
