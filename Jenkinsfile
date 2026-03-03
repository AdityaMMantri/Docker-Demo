pipeline {
    agent any

    environment {
        IMAGE_NAME = "adityammantri/flask-from-github"
    }

    stages {

        stage('Build Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Push Image') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-creds') {
                        dockerImage.push()
                    }
                }
            }
        }

    }
}
