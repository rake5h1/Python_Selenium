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

       stage('Install Pip') {
            steps {
                script {
                    // Download get-pip.py script
                    sh "curl -O https://bootstrap.pypa.io/get-pip.py"
                    // Install pip
                    sh "python get-pip.py"
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
