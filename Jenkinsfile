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
                    bat "curl -O https://bootstrap.pypa.io/get-pip.py"
                    // Install pip
                    bat "python get-pip.py"
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install required Python packages
                    bat "pip install -r req.txt"
                }
            }
        }
        stage('Download Edge WebDriver') {
            steps {
                script {
                    // Download and set up Edge WebDriver
                    bat "curl -O https://msedgedriver.azureedge.net/118.0.2088.76/edgedriver_linux64.zip"
                    bat "unzip edgedriver_linux64.zip"
                    bat "chmod +x msedgedriver"
                    bat "mv msedgedriver /usr/local/bin/"
                }
            }
        }

        stage('Run Behave Tests') {
            steps {
                script {
                    // Run Behave tests
                    bat "behave"
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
