import os

def docker_login(username, password):

    if username and password:
        print(f"{username} exist and  you are login sucessfully")

    else:
        print("User doesnot exist")


def main():
    username = os.environ.get("username")
    password = os.environ.get("password")

    docker_login(username, password)

if __name__ == "__main__":
    main()


