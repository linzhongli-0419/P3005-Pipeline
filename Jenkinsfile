pipeline {
   agent any
   stages {
      stage('Super long name case display view ONES Devops display ces12') {
         steps {
            echo 'Hello World'
         }
      }
      stage('Example test001') {
         steps {
            echo 'test001'
         }
      }
      stage('Example test002') {
         steps {
            echo 'test002'
         }
      }
      stage('Example test003') {
         steps {
            echo 'test003'
         }
      }
      stage('Example test004') {
         steps {
            echo 'test004'
         }
      }
      stage('Example test005') {
         steps {
            echo 'test005'
         }
      }
      stage('Example test006') {
         steps {
            echo 'test006'
         }
      }
      stage('Example test007') {
         steps {
            echo 'test007'
         }
      }
      stage('Example test008') {
         steps {
            echo 'test008'
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