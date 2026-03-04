pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-from-github"
        CONTAINER_NAME = "flask-demo"
    }

    stages {

        stage('Build Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%BUILD_NUMBER% ."
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    bat "docker tag %IMAGE_NAME%:%BUILD_NUMBER% %DOCKER_USER%/%IMAGE_NAME%:%BUILD_NUMBER%"
                    bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"
                    bat "docker push %DOCKER_USER%/%IMAGE_NAME%:%BUILD_NUMBER%"
                }
            }
        }

        stage('Run Container') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    bat """
                    docker stop %CONTAINER_NAME% || echo not running
                    docker rm %CONTAINER_NAME% || echo not existing
                    docker run -d --name %CONTAINER_NAME% -p 5000:5000 %DOCKER_USER%/%IMAGE_NAME%:%BUILD_NUMBER%
                    """
                }
            }
        }
    }
}
