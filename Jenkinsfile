pipeline {
   agent any
   stages {
      stage('Super long name case display view ONES Devops display ces12') {
         steps {
            echo 'Build runing......'
            sh "pwd"
            sh "mkdir ONES-Devops1"
            sh "ls"
            sh "ls -l"
            echo "打印长度。。。"
            sh "touch filename.txt"
            sh "ls"
            //sh "cd /var/jenkins_home/workspace/test001-01"
            sh "cat filename.txt"
            sleep 1
            echo 'two......'
            sh "pwd"
            sh "mkdir ONES-Devops3"
            sh "ls"
            sh "ls -l"
            sh "rm -rf ONES-Devops"
            sh "rm -rf ONES-Devops1"
            sh "rm -rf ONES-Devops3"
            sh "rm -rf filename.txt"
            echo "打印长度。。。."
            echo "打印长度。。。"
            echo "打印长度。。。"
            echo "打印长度。。。"
            echo "打印长度。。。"
            echo "打印长度。。。"
            echo "打印长度。。。"
            echo "打印长度。。。"
            echo "打印长度。。。"
            echo "打印长度。。。"
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