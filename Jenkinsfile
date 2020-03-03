pipeline {
   agent any
   environment {
       BranchName="Newmaster2"
   }
   stages {
      stage('Start build') {
         steps {
            sh 'pwd'
            sleep 15
            dir('/var/jenkins_home/workspace') {
               sh 'pwd'
            }
            echo 'Build runing'
            sleep 15
            sh "ps -a"
            sleep 15
            echo 'runing......'
         }
      }
      stage('Test environment'){
         when {
            branch 'master'
         }
         steps {
           sh "ls"
           echo "runing master"
         }
      }
      stage('Super long name case display') {
         environment {Description="This is "}
         steps{
            script{
               if (env.GIT_BRANCH == 'origin/Newmaster2'){
                  sleep 15
                  sh "ps -ef"
                  sleep 15
                  echo "${Description}${BranchName}"
                  sleep 15
               }
            }
         }
      }
   }
}



