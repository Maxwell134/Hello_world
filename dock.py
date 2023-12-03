import os
import subprocess
from  requests import status_codes

def docker_login(username, password):

    if username and password:
        
        login_command = f"docker login -u {username} -p {password}"
        login_docker = subprocess.run(login_command, shell=True, capture_output=True, text=True)

        if login_docker:
            print(f"{username} exist")
        else:
            print("Not correct")    

    else:
        print("User doesnot exist")


def main():
    username = os.environ.get("username")
    password = os.environ.get("password")

    docker_login(username, password)

if __name__ == "__main__":
    main()


