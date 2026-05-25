pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Krrish1901/student-performance-prediction.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install --break-system-packages pandas scikit-learn joblib'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python3 train_model.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t student-performance-prediction .'
            }
        }
    }
}
