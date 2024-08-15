import json
import os
import subprocess

file_path = 'pipeline.json'


def docker_pull(image_name, tag):
    try:
        if not image_name:
            raise ValueError("Image name is required for docker pull.")

        # Pull the Docker image
        subprocess.run(["docker", "pull", f"{image_name}:{tag}"], check=True)
        print(f'Docker image {image_name}:{tag} pulled successfully.')

    except subprocess.CalledProcessError:
        print(f'Error: Failed to pull Docker image {image_name}:{tag}.')
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')


def main():
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)

        if config.get('use_default_image', False):
            image_name = config.get('default_image', '')
        else:
            image_name = os.getenv('default_image')

        tag = 'latest'  # or any other tag you want to use

        # Ensure image_name is not empty
        if not image_name:
            raise ValueError("Image name is not set in pipeline.json or environment variables.")

        # Call docker_pull function
        docker_pull(image_name=image_name, tag=tag)

    except FileNotFoundError:
        print(f'Error: The file {file_path} does not exist.')
    except json.JSONDecodeError:
        print(f'Error: The file {file_path} is not a valid JSON file.')
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')


if __name__ == "__main__":
    main()
