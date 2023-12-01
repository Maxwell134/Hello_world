import subprocess
import sys

def login_to_docker(username, password):
    subprocess.run(['docker', 'login', '-u', username, '-p', password])

def pull_docker_image(image_name):
    subprocess.run(['docker', 'pull', image_name])

def run_docker_container(image_name, port_mapping):
    subprocess.run(['docker', 'run', '-d', '-p', port_mapping, image_name])

if __name__ == "__main__":
    # Input parameters from GitHub Actions YAML
    docker_username = sys.argv[0]
    docker_password = sys.argv[1]
    docker_image = sys.argv[2]
    port_mapping = sys.argv[3]

    # Login to Docker
    login_to_docker(docker_username, docker_password)

    # Pull Docker image
    pull_docker_image(docker_image)

    # Run Docker container
    run_docker_container(docker_image, port_mapping)
