pipeline {
   agent any
   stages {
      stage('Super long name case display, view ONES Devops display Q K') {
         steps {
            echo 'Hello World'
         }
      }
      stage('Example when') {
         when {
            branch 'Newmaster2'
         }
         steps{
            echo "执行该步骤steps"
         }
      }
      stage('Super long name case display, view ONES Devops display Q K') {
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