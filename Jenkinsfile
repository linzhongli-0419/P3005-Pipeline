pipeline {
   agent any
   stages {
      stage('Super long name case display view ONES Devops display ces12') {
         steps {
            echo 'Build runing......'
            sh "pwd"
            sh "mkdir ONES-Devops"
            sh "ls"
            sh "ls -l"
            echo "打印长度。。。"
            sh "mkdir test.txt"
            sh "cat test.txt"
            sleep 1
         }
      }
      stage('单元测试0010'){
         when {
             branch 'Newmaster2'
         }
         steps {
           echo '单元测试ing....'
           sh "pwd"
           sh "ps -ef"
         }
      }
      stage('Super long name case display, view ONES Devops display juhs') {
         steps{
            script{
               if (env.GIT_BRANCH == 'origin/Newmaster2'){
                  sleep 2
                  echo "end runing......"
               }
            }
         }
      }
   }
}