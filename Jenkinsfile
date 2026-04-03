pipeline {
    agent any

    environment {
        IMAGE_NAME = "robinspt/todo-app"
        IMAGE_TAG = "v1"
        CONTAINER_NAME = "todo-container"
        PORT = "5000"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "📥 Cloning repository..."
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker image..."
                sh '''
                    docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('Login to DockerHub') {
            steps {
                echo "🔐 Logging into DockerHub..."
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_TOKEN'
                )]) {
                    sh '''
                        echo "$DOCKER_TOKEN" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "📦 Pushing image to DockerHub..."
                sh '''
                    docker push $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                echo "🚀 Deploying container..."

                sh '''
                    # Stop old container if exists
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true

                    # Run new container
                    docker run -d \
                        -p $PORT:$PORT \
                        --name $CONTAINER_NAME \
                        $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }
    }

    post {
        always {
            echo "🧹 Cleaning up..."

            sh '''
                docker logout || true
            '''

            cleanWs()
        }

        success {
            echo "✅ Deployment successful!"
        }

        failure {
            echo "❌ Pipeline failed. Check logs."
        }
    }
}