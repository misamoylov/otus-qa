pipeline {
    agent {
        docker { image 'eeacms/pep8' }
    }
    stages {
        stage ("Code pull"){
            steps{
                checkout scm
            }
        }
        stage('Clone repo') {
            steps {
                sh 'rm -rf env'
                git url: 'https://github.com/misamoylov/otus-qa.git'
            }
        }
        stage('Run pep8'){
            steps {
                sh 'pep8 *'
            }
        }
    }
}