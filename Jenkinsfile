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
            branch 'Newmaster2'
         }
         steps{
            echo "when run master......."
         }
      }
      stage('test') {
         steps{
            script{
               if (env.GIT_BRANCH == 'origin/test'){
                  sleep 1
                  echo "run test..."
               }
            }
         }
      }
   }
}