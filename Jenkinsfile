pipeline {
   agent any
   stages {
      stage('branch-Newmaster2') {
         steps{
            script{
               if (env.GIT_BRANCH == 'origin/Newmaster2'){
                  sleep 20
                  echo "if run Newmaster2......."
               }
            }
         }
      }

      stage('branch-master') {
         when { branch 'Newmaster2' }
         steps{
            echo "when run master......."
         }
      }

      stage('test') {
         steps{
            script{
               if (env.GIT_BRANCH == 'origin/test'){
                  sleep 20
                  echo "run test..."
               }
            }
         }
      }
   }
}