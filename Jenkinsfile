pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/02fe23bcs060-commits/devops-monitoring.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t devops-monitoring .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 devops-monitoring'
            }
        }
    }
}