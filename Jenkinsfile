pipeline {
  agent {
    docker {
      image 'ones-api-env'
      args '-v /srv/project-govendor-cache:/go/.cache'
    }
  }

  options {
    timeout(time: 20, unit: 'MINUTES')
    disableConcurrentBuilds()
  }

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
          if (env.BRANCH_NAME == "master"){
            //检测是 PR, 如“Merge pull request #2328 from BangWork/F9016)“, 则自动编译脚本 migrate-F9016
            def pr_name = sh (script: 'git log -1 --pretty=format:"%s"| grep "Merge pull request" | awk -F "/" \'{print $2}\'', returnStdout: true).trim()
            env.MIGRATION_NAME = pr_name
          }else{
            env.MIGRATION_NAME = env.BRANCH_NAME
          }
          sh '''
          echo "MIGRATION_NAME: $MIGRATION_NAME"
          #如果没有 BRANCH_NAME 变量中止构建
          [[ "${BRANCH_NAME}" == "" ]] && echo "empty BRANCH_NAME" && exit 1 || true
          '''
        }
      }
    }

    stage('编译,打包') {
      options {
        retry(1)
      }
      steps {
        withCredentials(
          bindings: [usernamePassword(credentialsId: 'web_github_token', \
                     usernameVariable: 'GITHUB_USER', \
                     passwordVariable: 'GITHUB_ACCESS_TOKEN')
        ]) {
          sh '''
            git config --global url."https://${GITHUB_ACCESS_TOKEN}:x-oauth-basic@github.com/".insteadOf "https://github.com/"
            /bin/bash devops/build.sh --tar-name=${TAR_FILE_NAME} --migration-name=${MIGRATION_NAME}
          '''
        }
      }
    }

    stage('配置替换') {
      steps {
        withCredentials([
          file(credentialsId: 'CONFIG_FILE', variable: 'APP_CONFIG_FILE'),
          file(credentialsId: 'ES_CONFIG_FILE', variable: 'ES_CONFIG_FILE'),
          string(credentialsId: 'DB_PASSWORD', variable: 'DB_PASSWORD')
        ]) {
          sh '''
            /bin/bash devops/test/conf.sh
          '''
        }
        /**
        script {
          sh '''
            # 如果配置文件不需要替换，直接使用以下操作
            #echo "## Copy config ..."
            #echo "cp ${APP_CONFIG_FILE} ${DEST_DIR}/"
            #echo "cp ${ES_CONFIG_FILE} ${DEST_DIR}/es_config.json"
          '''
        }
        **/
      }
    }

    stage('部署服务') {
      /**
      when {
        not {
          branch 'master'
        }
      }
      **/
      steps {
        withCredentials([
          sshUserPrivateKey(credentialsId: 'dev.ones.team', keyFileVariable: 'SSH_PRIVATE_KEY'),
          string(credentialsId: 'DB_PASSWORD', variable: 'DB_PASSWORD')
        ]) {
            sh '''
               echo "cp devops/test/*.sh ${DEST_DIR}/"
               cp devops/remote/*.sh ${DEST_DIR}/
               cat ${SSH_PRIVATE_KEY} > ~/.ssh/id_rsa && chmod 400 ~/.ssh/id_rsa
               /bin/bash devops/test/deploy.sh
            '''
        }
      }
    }
  }

  post {
    always {
      echo 'Pipeline finished, Pushing notification now ...'
    }
    success {
      sh '/bin/bash devops/notify.sh success'
    }
    unsuccessful {
      sh '/bin/bash devops/notify.sh unsuccessful'
    }
  }

}