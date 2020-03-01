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
       stage('提交测试') {
          parallel {
             stage('代码分析'){
                steps {
                   echo '代码分析ing...'
                   echo '代码分析完成...'
                  }
              }
             stage('单元测试001'){
                steps {
                   echo '单元测试ing....'
                   echo '单元测试完成.....'
                   }
               }
             stage('单元测试002'){
                steps {
                   echo '单元测试ing....'
                   echo '单元测试完成.....'
                   }
               }
             stage('单元测试003'){
                steps {
                   echo '单元测试ing....'
                   echo '单元测试完成.....'
                   }
               }
             stage('单元测试004'){
                steps {
                   echo '单元测试ing....'
                   echo '单元测试完成.....'
                   }
               }
             stage('单元测试005'){
                steps {
                   echo '单元测试ing....'
                   echo '单元测试完成.....'
                   }
               }
             stage('单元测试006'){
                steps {
                   echo '单元测试ing....'
                   echo '单元测试完成.....'
                   }
               }
             stage('单元测试007'){
                steps {
                   echo '单元测试ing....'
                   echo '单元测试完成.....'
                   }
               }
             stage('单元测试008'){
                steps {
                   echo '单元测试ing....'
                   echo '单元测试完成.....'
                   }
               }
             stage('单元测试009'){
                steps {
                   echo '单元测试ing....'
                   echo '单元测试完成.....'
                   }
               }
             stage('单元测试0010'){
                steps {
                   echo '单元测试ing....'
                   echo '单元测试完成.....'
                   }
               }
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