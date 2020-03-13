pipeline {
    agent any
    stages {
       stage('Build') {
             steps {
                echo '编译'
            }
        }
       stage('代码编译') {
          parallel {
             stage('代码分析'){
                steps {
                   echo '代码分析ing...'
                   echo '代码分析完成...'
                  }
              }
              stage('单元测试'){
              when {
                   branch "master"
              }
                 steps {
                   echo '单元测试ing....'
                   echo '单元测试完成.....'
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