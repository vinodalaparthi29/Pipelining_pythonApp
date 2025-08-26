pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {
        stage('Clone GitHub Repo') {
            steps {
                git branch: 'main', credentialsId: 'github-https', url: 'https://github.com/vinodalaparthi29/Pipelining_pythonApp.git'
            }
        }

        stage('Set Up Python Virtual Environment') {
            steps {
                bat '"C:\\Users\\vinodalaparthi29\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m venv venv'
                bat '.\\venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.\\venv\\Scripts\\pip install flask pandas numpy tensorflow' 
            }
        }

        stage('Run Flask App') {
            steps {
                bat '.\\venv\\Scripts\\python app.py'
            }
        }
    }
}
