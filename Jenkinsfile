pipeline {

    agent any

    stages {

        stage('Install Dependencies') {

            steps {

                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Pytest Suite') {

            steps {

                bat 'pytest -n 2 --html=reports/report.html --self-contained-html'
            }
        }

        stage('Generate Allure Results') {

            steps {

                bat 'pytest --alluredir=allure-results'
            }
        }
    }

    post {

        always {

            archiveArtifacts artifacts: 'reports/*'

            archiveArtifacts artifacts: 'screenshots/*'

            archiveArtifacts artifacts: 'logs/*'
        }
    }
}