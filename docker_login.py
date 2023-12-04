import os
import subprocess
import requests

def check_docker_image_exists(image_name, username, password):
    # Login to Docker Hub
    docker_login_cmd = f'docker login -u {username} -p {password}'
    api_url = f'https://hub.docker.com/v2/repositories/{username}/{image_name}/tags'
    
    subprocess.run(docker_login_cmd, shell=True, check=True)

    response = requests.get(api_url)

    # Check if the image exists
    docker_pull_cmd = f'docker pull {image_name}'
    pull_result = subprocess.run(docker_pull_cmd, shell=True, stderr=subprocess.PIPE)

    if response.status_code == 200:
        print(f"Image {image_name} exists on Docker Hub.")
        return "exist"
    elif response.status_code == 404:
        print(f"Image {image_name} does not exist on Docker Hub.")
        return "none"
    else:
        print(f"Failed to check the status of the image on Docker Hub. Status code: {response.status_code}")
        return "error"

if __name__ == "__main__":
    image_name = os.environ.get('INPUT_IMAGE')
    docker_username = os.environ.get('DOCKER_USERNAME')
    docker_password = os.environ.get('DOCKER_PASSWORD')

    image_exists = check_docker_image_exists(image_name, docker_username, docker_password)

    # Output result for GitHub Actions
    print(f"::set-output name=image_exists::{str(image_exists).lower()}")
