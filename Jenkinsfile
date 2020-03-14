pipeline {
    agent any
    stages {
       stage('Build') {
             steps {
                sleep 15
                echo '编译'
            }
        }
       stage('代码编译') {
          parallel {
             stage('代码分析'){
                when {
                   branch 'master'
                }
                steps {
                   sleep 15
                   echo '代码分析ing...'
                   echo '代码分析完成...'
                  }
              }
              stage('单元测试'){
                 steps {
                   echo '测试ing....'
                   echo '单元测试完成.....'
                   }
               }
           }
       }
        stage('验收阶段') {
          parallel {
              stage('环境测试'){
                when {
                   branch 'master'
                }
                steps {
                    echo 'Test Module1--01 stage ...'
                    }
                }
              stage('接口测试') {
                 steps {
                    echo 'Test Module1--02 stage ...'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}