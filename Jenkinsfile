pipeline {
   agent any
   stages {
      stage('master') {
         steps{
            script{
               if (env.GIT_BRANCH == 'origin/master'){
                  echo "run master......."
               }
            }
         }
      }

      stage('branch') {
         when { branch 'master' }
         steps{
            echo "run master......."
         }
      }

      stage('test') {
         steps{
            script{
               if (env.GIT_BRANCH == 'origin/test'){
                  echo "run test..."
               }
            }
         }
      }
   }
}