@Library("shared")_
pipeline {
    agent {label "vinod"} 
    
    stages{
        stage("Clone Code"){
            steps {
                echo "Cloning the code"
                git url:"https://github.com/MonikaWalanj/devops-webapp.git", branch: "main"
				echo "Code cloning successful"
            }
        }
        stage("Build"){
            steps {
                echo "Building the image"
                sh "docker build -t notes-app:latest ."
            }
        }
        stage("Push to Docker Hub"){
            steps {
                script{
                    docker_push("notes-app","latest","monikawalanj")
                }
            }
        }
        stage("Deploy"){
            steps {
                echo "Deploying the container"
                sh "docker run -d -p 8000:8000 notes-app:latest"
                
            }
        }
    }
}
