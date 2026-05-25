pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Krrish1901/student-performance-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python train_model.py'
            }
        }

        stage('Run Prediction') {
            steps {
                bat 'python predict.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-performance .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run --name student-container student-performance'
            }
        }
    }
}
