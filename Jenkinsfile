pipeline {
   agent any
   environment {
       BranchName="P3005-Pipelien"
   }
   stages {
      stage('Start build') {
         steps {
            echo 'pwd'
            //sleep 36
            sleep 15
            //dir('/var/jenkins_home/workspace') {
               //sh 'ps'
            //}
            echo 'Build runing'
            sh "ps -a"
         }
      }
      stage('Code.......'){
         steps {
           echo "This is Codeing......"
           sleep 15
           //sh "ls -l"
           //sh "pwd"
           echo "runing master"
         }
      }
      stage('Test runing'){
         when {
            branch 'master'
         }
         steps {
           sleep 15
           echo "runing master"
         }
      }
      stage('Deploy ending') {
         environment {Description="This is "}
         steps{
            script{
               if (env.GIT_BRANCH == 'origin/P3005-Pipelien'){
                  echo "${Description}${BranchName}"
                  sleep 25
                  sh "ls"
               }
            }
         }
      }
   }
}
