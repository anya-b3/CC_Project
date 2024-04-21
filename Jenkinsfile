pipeline {
    agent any
    environment {
        KUBECONFIG = credentials('mykubeconfig')  
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], 
                          doGenerateSubmoduleConfigurations: false, extensions: [],
                          submoduleCfg: [], 
                          userRemoteConfigs: [
                              [url: 'https://github.com/anya-b3/CC_Project.git']
                          ]
                ])
            }
        }

        stage('Build and Test') {
            steps {
                // Add build and test steps for each service if required
                dir('product-service') {
                    // Example: sh 'mvn clean package'
                }
                dir('order-service') {
                    // Example: sh 'mvn clean package'
                }
                dir('login-service') {
                    // Example: sh 'mvn clean package'
                }
                dir('mongodb') {
                    // Example: sh 'mvn clean package'
                }
                dir('add_product_db') {
                    // Example: sh 'mvn clean package'
                }
                dir('ui') {
                    // Example: npm install && npm run build
                }
                dir('ui/login') {
                    // Example: docker build -t your_docker_image_name .
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                // Add build Docker image steps for each service if required
                dir('product-service') {
                    script{
                        docker.build('wubbles1012/product-service:latest')
                        docker.withRegistry('https://index.docker.io/v1/', 'docker_name_pass') {
                            // Tag the Docker image with the Docker Hub repository name
                            docker.image('wubbles1012/product-service:latest').push()
                        }
                    }
                }
                dir('order-service') {
                    // Example: docker.build('your_docker_image_name')
                }
                dir('login-service') {
                    // Example: docker.build('your_docker_image_name')
                }
                dir('mongodb') {
                    // Example: docker.build('your_docker_image_name')
                }
                dir('add_product_db') {
                    // Example: docker.build('your_docker_image_name')
                }
                dir('ui') {
                    // Example: docker.build('your_docker_image_name')
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Apply Kubernetes deployment and service files
                    bat 'kubectl apply -f product-deployment.yaml'
                    bat 'kubectl apply -f product-service.yaml'
                    bat 'kubectl apply -f order-deployment.yaml'
                    bat 'kubectl apply -f order-service.yaml'
                    bat 'kubectl apply -f loginui-deployment.yaml'
                    bat 'kubectl apply -f loginui-service.yaml'
                    bat 'kubectl apply -f mongodb-deployment.yaml'
                    bat 'kubectl apply -f flask-deployment.yaml'
                    bat 'kubectl apply -f flask-service.yaml'
                    // Add more apply commands if needed
                }
            }
        }
    }
}
