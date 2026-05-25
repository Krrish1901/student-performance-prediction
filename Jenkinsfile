pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/Krrish1901/student-performance-prediction.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install pandas scikit-learn joblib'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python train_model.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t student-performance-prediction .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run student-performance-prediction'
            }
        }
    }
}
