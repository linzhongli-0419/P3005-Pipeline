pipeline {
   agent any
   environment {
       BranchName="Newmaster2"
   }
   stages {
      stage('Start build') {
         steps {
            sh 'pwd'
            sleep 10
            dir('/var/jenkins_home/workspace') {
               sh 'pwd'
            }
            echo 'Build runing'
            echo 'runing......'
            sh "ps -a"
         }
      }
      stage('Code compilation'){
         steps {
           echo "This is Codeing......"
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
                  sleep 30
                  sh "ps -ef"
               }
            }
         }
      }
   }
}



