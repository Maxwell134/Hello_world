import json
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
    print(f"::set-output name=build_status::{result}")

if __name__ == '__main__':
    main()
