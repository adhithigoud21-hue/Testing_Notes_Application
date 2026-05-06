pipeline {

    agent any

    stages {

        stage('Install Dependencies') {

            steps {

                bat '"C:\\Users\\rohit\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest Suite') {

            steps {

                bat '"C:\\Users\\rohit\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m pytest -n 2 --html=reports/report.html --self-contained-html'
            }
        }

        stage('Generate Allure Results') {

            steps {

                bat '"C:\\Users\\rohit\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m pytest --alluredir=allure-results'
            }
        }
    }

    post {

    always {

        archiveArtifacts artifacts: 'reports/*', allowEmptyArchive: true

        archiveArtifacts artifacts: 'screenshots/*', allowEmptyArchive: true

        archiveArtifacts artifacts: 'logs/*', allowEmptyArchive: true

        archiveArtifacts artifacts: 'allure-results/*', allowEmptyArchive: true
    }
}
    }
