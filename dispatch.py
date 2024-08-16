import json
import requests
import os

def run():
    # Fetch the environment variables
    repo = os.getenv('INPUT_REPO')
    event_type = os.getenv('INPUT_EVENT_TYPE')
    token = os.getenv('INPUT_TOKEN')

    # Validate inputs
    if not repo:
        raise ValueError("Input 'repo' is not set. Please provide the repository in the format 'owner/repo'.")
    if not event_type:
        raise ValueError("Input 'event_type' is not set. Please provide the event type.")
    if not token:
        raise ValueError("Input 'token' is not set. Please provide the GitHub token.")

    owner, repo_name = repo.split('/')
    url = f'https://api.github.com/repos/{owner}/{repo_name}/dispatches'

    headers = {
        'Authorization': f'token {token}',
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

if __name__ == "__main__":
    run()
