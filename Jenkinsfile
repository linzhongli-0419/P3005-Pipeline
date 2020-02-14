pipeline {
   agent any
   stages {
      stage('构建') {
         steps {
            echo 'Hello World'
         }
      }
      stage('审查') {
         steps {
            //sleep 60
            python Hello.py
         }
      }
   }
}
