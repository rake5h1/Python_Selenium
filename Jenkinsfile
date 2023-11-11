pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.8'  // Change this to your desired Python version
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Set Up Python') {
            steps {
                script {
                    // Install and set up Python
                    sh "pyenv install -s ${PYTHON_VERSION}"
                    sh "pyenv global ${PYTHON_VERSION}"
                    sh "python -m venv venv"
                    sh "source venv/bin/activate"
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install required Python packages
                    sh "pip install -r req.txt"
                }
            }
        }
        stage('Download Edge WebDriver') {
            steps {
                script {
                    // Download and set up Edge WebDriver
                    sh "curl -O https://msedgedriver.azureedge.net/118.0.2088.76/edgedriver_linux64.zip"
                    sh "unzip edgedriver_linux64.zip"
                    sh "chmod +x msedgedriver"
                    sh "mv msedgedriver /usr/local/bin/"
                }
            }
        }

        stage('Run Behave Tests') {
            steps {
                script {
                    // Run Behave tests
                    sh "behave"
                }
            }
        }

     
    }

    post {
        always {
            // Clean up workspace
            cleanWs()
        }
    }
}
