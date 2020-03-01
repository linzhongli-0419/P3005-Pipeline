pipeline {
   agent any
   stages {
      stage('Super long name case display view ONES Devops display ces12') {
         steps {
            echo 'Hello World'
         }
      }
      stage('单元测试0010'){
         steps {
           echo '单元测试ing....'
           sh "pw"
         }
      }
      stage('Super long name case display, view ONES Devops display juhs') {
         steps{
            script{
               if (env.GIT_BRANCH == 'origin/Newmaster2'){
                  sleep 1
                  echo "run test..."
               }
            }
         }
      }
   }
}