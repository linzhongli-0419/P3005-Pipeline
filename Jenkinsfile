pipeline {
   agent any
   stages {
      stage('Super long name case display view') {
         steps {
            echo 'Build runing......'
            sh "pwd"
         }
      }
      stage('单元测试ing'){
         steps {
           sh "pwd"
           sh "ps -ef"
         }
      }
      stage('Super long name case display') {
         steps{
            script{
               if (env.GIT_BRANCH == 'origin/Newmaster2'){
                  sleep 1
                  echo "end runing......"
               }
            }
         }
      }
   }
}