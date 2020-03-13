pipeline {
    agent any
    stages {
       stage('Build') {
          steps {
            sleep 20
            echo '编译'
            }
        }
       stage('代码编译') {
          parallel {
             stage('代码分析'){
                steps {
                   echo '代码分析ing...'
                   sleep 20
                   echo '代码分析完成...'
                  }
              }
              stage('单元测试'){
                 steps {
                   echo '单元测试ing....'
                   sleep 20
                   echo '单元测试完成.....'
                   }
               }
            stage('单元测试1'){
                 steps {
                   echo '单元测试ing....'
                   sleep 20
                   echo '单元测试完成.....'
                   }
               }
            stage('单元测试2'){
                 steps {
                   echo '单元测试ing....'
                   sleep 20
                   echo '单元测试完成.....'
                   }
               }
            stage('单元测试3'){
                 steps {
                   echo '单元测试ing....'
                   sleep 20
                   echo '单元测试完成.....'
                   }
               }
            stage('单元测试4'){
                 steps {
                   echo '单元测试ing....'
                   sleep 20
                   echo '单元测试完成.....'
                   }
               }
            stage('单元测试5'){
                 steps {
                   echo '单元测试ing....'
                   sleep 20
                   echo '单元测试完成.....'
                   }
               }
           }
       }
       stage('Deploy') {
            steps {
                sleep 20
                echo 'Deploying....'
            }
        }
    }
}