# docker_login.py

import subprocess
import sys

def docker_login(username, password):
    try:
        login_cmd = f"docker login -u {username} --password-stdin"
        subprocess.run(login_cmd, input=password, shell=True, check=True)
        print("Docker login successful.")
    except subprocess.CalledProcessError as e:
        print(f"Docker login failed. Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    docker_username = sys.argv[1]
    docker_password = sys.argv[2]

    docker_login(docker_username, docker_password)
