import json
import os

def check_parameter(filename):
    with open(filename, 'r') as file:
        config = json.load(file)
        set_flag = config.get('use_default_image', False)
        if set_flag:
            return "proceed"
        else:
            return "skip"

def main():
    result = check_parameter('pipeline.json')
    # Write the result to the GITHUB_ENV file
    with open(os.getenv('GITHUB_ENV', ''), 'a') as f:
        f.write(f"build_status={result}\n")

if __name__ == '__main__':
    main()
