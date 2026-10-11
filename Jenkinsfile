
pipeline {
    agent any

    stages {
        stage('Clone Source Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cloud-app .'
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    docker stop cloud-app || true
                    docker rm cloud-app || true
                    docker run -d --restart unless-stopped --name cloud-app -p 5000:5000 cloud-app
                '''
            }
        }
    }
}