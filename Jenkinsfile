pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'calculator_python'
        GITHUB_REPO_URL = 'https://github.com/dibyaruppal/spe_mini_project.git'
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the code from the GitHub repository
                    git branch: 'main', url: "${GITHUB_REPO_URL}"
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE_NAME}", '.')
                }
            }
        }
        stage('Push Docker Images') {
            steps {
                script{
                    docker.withRegistry('', 'DockerHubCredential') {
                    sh 'docker tag calculator_python dibyaruppal/calculator_python:latest'
                    sh 'docker push dibyaruppal/calculator_python'
                    }
                 }
            }
        }
   stage('Run Ansible Playbook') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'inventory'
                     )
                }
            }
        }

    }
}