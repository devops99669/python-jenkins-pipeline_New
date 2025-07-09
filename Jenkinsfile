pipeline {
    agent any

    stages {
        stage('Run Python Script') {
            steps {
                echo '🔧 Running app.py using shell'
                sh 'python3 app.py'
            }
        }
    }

    post {
        always {
            echo '✅ Job completed'
        }
    }
}

