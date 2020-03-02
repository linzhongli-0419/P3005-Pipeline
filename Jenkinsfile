pipeline {
   agent any
   stages {
      stage('构建') {
         steps {
            echo 'Hello World'
         }
      }
      stage('test'){
         steps{
            echo 'test 01...'
            echo 'test 02...'
            echo 'test 03 03...'
         }
      }
      stage('审查') {
         steps {
            //sleep 60
            echo '审查'
         }
      }
      stage('DevOps') {
         steps {
            echo 'ending........'
         }
      }
   }
}
