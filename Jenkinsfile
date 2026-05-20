pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/YOUR_USERNAME/devops-monitoring.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t devops-monitoring .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run -d -p 5000:5000 devops-monitoring'
            }
        }

    }
}