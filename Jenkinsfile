pipeline {
    agent any
    tools {
        python 'Python3'  // Jenkins > Global Tool Configuration > Add Python tool
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Selenium Tests') {
            steps {
                sh 'pytest tests/test_login.py --html=report.html'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}
