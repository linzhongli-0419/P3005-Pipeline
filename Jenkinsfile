pipeline {
   agent any
   environment {
       BranchName="Newmaster2"
   }
   stages {
      stage('Start build') {
         steps {
            dir('/var/jenkins_home/workspace') {
               sh 'pwd'
         }
            echo 'Build runing'
            sleep 30
            sh "ps -a"
            sleep 15
            echo 'runing......'
         }
      }
      stage('Select test environment'){
         when {
            branch 'master'
         }
         steps {
           sh "ls"
           echo "runing master"
         }
      }
      stage('Super long name case display') {
         steps{
            environment {Description="This is"}
            script{
               if (env.GIT_BRANCH == 'origin/Newmaster2'){
                  sleep 1
                  sh "ps -ef"
                  echo "${Description}${BranchName}"
               }
            }
         }
      }
   }
}



