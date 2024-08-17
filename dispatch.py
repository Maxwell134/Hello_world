import os
import json
import requests

def run():
    repo_name = os.getenv('INPUT_REPO_NAME')  # GitHub Actions input parameter
    event_type = os.getenv('INPUT_EVENT_TYPE')  # GitHub Actions input parameter
    token = os.getenv('INPUT_TOKEN')  # GitHub Actions input parameter

    if not repo_name or not event_type or not token:
        raise ValueError("One or more required environment variables are not set.")

    print(f"Repo Name: {repo_name}")
    print(f"Event Type: {event_type}")
    print(f"Token: {token[:5]}...")  # Partially masked token for debugging

    url = f'https://api.github.com/repos/{repo_name}/dispatches'
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github+json'
    }
    data = {
        'event_type': event_type
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    if response.status_code == 204:
        print(f"Dispatched event {event_type} to {repo_name}")
    else:
        print(f"Failed to dispatch event: {response.status_code} - {response.text}")
        response.raise_for_status()

if __name__ == '__main__':
    run()
