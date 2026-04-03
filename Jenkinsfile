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
                echo "🚀 Deploying containers..."

                sh '''
                    # Create a custom Docker network
                    docker network create todo-network || true

                    # Stop & remove old database container if exists
                    docker stop todo-db || true
                    docker rm todo-db || true

                    # Stop & remove old app container if exists
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true

                    # Run the PostgreSQL database container
                    docker run -d \
                        --name todo-db \
                        --network todo-network \
                        --restart always \
                        -e POSTGRES_USER=postgres \
                        -e POSTGRES_PASSWORD=admin \
                        -e POSTGRES_DB=todo_db \
                        -v todo-db-data:/var/lib/postgresql/data \
                        postgres:15

                    # Pause briefly to allow Postgres to initialize
                    sleep 5

                    # Run the new application container connected to Postgres
                    docker run -d \
                        -p $PORT:$PORT \
                        --name $CONTAINER_NAME \
                        --network todo-network \
                        -e DATABASE_URL="postgresql://postgres:admin@todo-db:5432/todo_db" \
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