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
               sh 'ps'
            }
            sleep 15
            echo 'Build runing'
            echo 'runing......'
            sh "ps -a"
         }
      }
      stage('Code compilation'){
         steps {
           echo "This is Codeing......"
           sleep 20
           sh "ls -l"
           sh "pwd"
           echo "runing master"
         }
      }
      stage('Test runing'){
         when {
            branch 'master'
         }
         steps {
           sh "ls"
           echo "runing master"
         }
      }
      stage('Deploy ending') {
         environment {Description="This is "}
         steps{
            script{
               if (env.GIT_BRANCH == 'origin/Newmaster2'){
                  echo "${Description}${BranchName}"
                  sleep 21
                  sh "ps -ef"
               }
            }
         }
      }
   }
}



