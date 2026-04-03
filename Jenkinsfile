    pipeline {
        agent any

        environment {
            IMAGE_NAME = "robinspt/todo-app"
            IMAGE_TAG = "v1"
        }

        stages {
            stage('Checkout') {
                steps {
                    checkout scm
                }
            }

            stage('Build Docker Image') {
                steps {
                    sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
                }
            }

            stage('Push to DockerHub') {
                steps {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh '''
                            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                            docker push $IMAGE_NAME:$IMAGE_TAG
                        '''
                    }
                }
            }

            stage('Deploy with Docker Compose') {
                steps {
                    sh '''
                        docker-compose down || true
                        docker-compose pull || true
                        docker-compose up -d --build
                    '''
                }
            }
        }
        
        // Add a post section to gracefully clean up after execution
        post {
            always {
                // Logs out of docker hub
                sh 'docker logout || true'
                // Cleans up the Jenkins workspace to save space
                cleanWs()
            }
        }
    }
