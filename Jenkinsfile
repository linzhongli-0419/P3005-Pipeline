pipeline {
   agent any
   stages {
      stage('Example-ONES') {
         steps {
            echo 'Hello World'
         }
      }
      stage('Example when') {
         when {
            branch 'origin/Newmaster2'
         }
         steps{
            echo "执行该步骤steps"
         }
      }
      stage('test') {
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