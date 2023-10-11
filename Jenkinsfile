pipeline {
    agent {
        node {
            label 'docker'
        }
    }
    options {
        ansiColor('xterm')
        timeout(time: 30, unit:'MINUTES')
        timestamps()
        disableConcurrentBuilds()
    }
    stages {
        stage('Cleanup') {
            steps {
                // Clean out any old workspace files
                cleanWs()
                // Run `docker rmi` against every tag of an image to clear out any old images on the build server
                sh "docker images | grep nicholasjgraham/nickjgraham.com | tr -s ' ' | cut -d ' ' -f 2 | xargs -I _ docker rmi nicholasjgraham/nickjgraham.com:_"
                // Clean up any untagged images, more cleanup
                sh "docker image prune -f"
                // Check everything back out from git
                checkout scm
            }
        }
        stage('Docker Build') {
            steps {
                // Build our new image
                sh "docker build -t nicholasjgraham/nickjgraham.com:latest --build-arg BUILD_NUMBER=$BUILD_NUMBER --build-arg BRANCH_NAME=$BRANCH_NAME ."
            }
        }
        stage('Docker Run') {
            steps {
                // Start up a container that we can use to run testing and validation commands
                sh "docker run -d --name nickjgrahamcom-build nicholasjgraham/nickjgraham.com:latest"
            }
        }
        stage('Lint') {
            steps {
                // Run flake8 linting against the code inside the new container
                sh "docker exec -t nickjgrahamcom-build sh -c 'flake8; exit \$?'"
            }
        }
        stage('Test') {
            steps {
                // Try to hit the /health endpoint and make sure that's working
                sh "docker exec -t nickjgrahamcom-build sh -c 'curl -f http://localhost:8080/health; exit \$?'"
                // Try to hit / too
                sh "docker exec -t nickjgrahamcom-build sh -c 'curl -f http://localhost:8080/; exit \$?'"
                // Try to hit /about too
                sh "docker exec -t nickjgrahamcom-build sh -c 'curl -f http://localhost:8080/about; exit \$?'"
            }
        }
        stage('Push') {
            steps {
                // Push our new image up to docker hub
                sh "docker tag nicholasjgraham/nickjgraham.com:latest nicholasjgraham/nickjgraham.com:$BRANCH_NAME-$BUILD_NUMBER"
                sh "docker tag nicholasjgraham/nickjgraham.com:latest nicholasjgraham/nickjgraham.com:$BRANCH_NAME"
                sh "docker push -a nicholasjgraham/nickjgraham.com"
            }
        }
    }
    post {
        failure {
            script {
                // Get docker logs on failure in case any of our checks didn't work
                // Get running container ID
                containerID = sh(
                    script: "docker ps | sed -n 2p | awk '{print \$1;}'",
                    returnStdout: true
                )
                // Echo container logs
                sh "docker logs nickjgrahamcom-build"
            }
        }
        cleanup {
            // Stop the test container and delete it
            sh "docker stop nickjgrahamcom-build"
            sh "docker rm nickjgrahamcom-build"
        }
    }
}