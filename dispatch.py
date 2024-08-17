import os
import json
import requests

def run():
    repo_name = 'Maxwell134/K3s_set_up-in-aws'
    event_type = os.getenv('INPUT_EVENT_TYPE')
    token = os.getenv('INPUT_TOKEN')

    url = f'https://api.github.com/repos/{repo_name}/dispatches'

    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    data = {
        'event_type': event_type,
        'client_payload': {}
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 204:
        print(f"Dispatched event {event_type} to {repo_name}")
    else:
        print(f"Failed to dispatch event: {response.status_code} - {response.text}")
        response.raise_for_status()

if __name__ == '__main__':
    run()
