# docker_login.py
import subprocess
import sys
import os

def docker_login(username, password, registry):
    try:
        login_cmd = f"docker login -u {username} --password-stdin {registry}"
        subprocess.run(login_cmd, input=password.encode('utf-8'), shell=True, check=True)
        print("Docker login successful.")
    except subprocess.CalledProcessError as e:
        print(f"Docker login failed. Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    docker_username = os.getenv("DOCKER_USERNAME")
    docker_password = os.getenv("DOCKER_PASSWORD")
    docker_registry = os.getenv("DOCKER_REGISTRY", "docker.io")  # Default to Docker Hub

    docker_login(docker_username, docker_password, docker_registry)
