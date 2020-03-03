pipeline {
   agent any
   environment {
       BranchName="Newmaster2"
   }
   stages {
      stage('Start build') {
         steps {
            echo 'Build runing......'
            sleep 30
            sh "ps -a"
         }
      }
      stage('单元测试ing'){
         when {
            branch 'master'
         }
         steps {
           sh "pwd"
           echo ""
         }
      }
      stage('Super long name case display') {
         steps{
            script{
               if (env.GIT_BRANCH == 'origin/Newmaster2'){
                  sleep 1
                  sh "ps -ef"
                  echo "${BranchName}"
               }
            }
         }
      }
   }
}



