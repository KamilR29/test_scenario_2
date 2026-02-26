pipeline {
  agent any

  environment {
    PYTHON = "C:\\Users\\kamil.raczkowski\\AppData\\Local\\Programs\\Python\\Python314\\python.exe"
  }

  stages {
    stage('Setup') {
      steps {
        bat """
        "%PYTHON%" --version
        "%PYTHON%" -m venv .venv
        call .venv\\Scripts\\activate
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        """
      }
    }

    stage('Test') {
      steps {
        bat """
        call .venv\\Scripts\\activate
        python -m unittest discover -s test -p "test_*.py" -v
        """
      }
    }
  }
}