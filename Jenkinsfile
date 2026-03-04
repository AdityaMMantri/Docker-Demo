pipeline {
    agent any

    stages {

        stage('Build Image') {
            steps {
                bat "docker build -t flask-from-github:%BUILD_NUMBER% ."
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    bat """
                    docker tag flask-from-github:%BUILD_NUMBER% %DOCKER_USER%/flask-from-github:%BUILD_NUMBER%
                    docker login -u %DOCKER_USER% -p %DOCKER_PASS%
                    docker push %DOCKER_USER%/flask-from-github:%BUILD_NUMBER%
                    """
                }
            }
        }
    }
}
