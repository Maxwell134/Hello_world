import json
import requests
import os

def run():

    repo = os.getenv('INPUT_REPO')
    event_type = os.getenv('INPUT_EVENT_TYPE')
    token = os.getenv('INPUT_TOKEN')

    owner, repo_name = repo.split('/')
    url = f'https://api.github.com/repos/{owner}/{repo_name}/dispatches'

    headers = {

        'Authorization': f'{token}',
        'Accept': 'application/vnd.github.everest-preview+json'
    }

    data = {
        'event_type': event_type
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 204:
        print(f"Dispatched event {event_type} to {repo}")
    else:
        print(f"Failed to dispatch event: {response.status_code} - {response.text}")
        response.raise_for_status()

if __name__ == '__main__':
    run()
