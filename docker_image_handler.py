import json
import subprocess
import sys

def load_pipeline_config(filename="pipeline.json"):
    with open(filename, "r") as f:
        return json.load(f)

def docker_pull(image_name):
    try:
        subprocess.run(["docker", "pull", image_name], check=True)
        print(f"Successfully pulled image: {image_name}")
    except subprocess.CalledProcessError:
        print(f"Failed to pull image: {image_name}")
        sys.exit(1)

def docker_tag(source_image, target_image):
    try:
        subprocess.run(["docker", "tag", source_image, target_image], check=True)
        print(f"Successfully tagged image: {source_image} as {target_image}")
    except subprocess.CalledProcessError:
        print(f"Failed to tag image: {source_image}")
        sys.exit(1)

def main():
    config = load_pipeline_config()

    if config["use_default_image"]:
        image_name = config["default_image"]
    else:
        if not config["custom_image"]:
            print("Error: No custom image provided in pipeline.json.")
            sys.exit(1)
        image_name = config["custom_image"]

    docker_pull(image_name)
    docker_tag(image_name, "your-dockerhub-username/your-image-name:latest")

if __name__ == "__main__":
    main()
