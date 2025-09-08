import os
import json

event_path = os.getenv('GITHUB_EVENT_PATH')

if event_path and os.path.exists(event_path):
    with open(event_path, 'r') as f:
        event = json.load(f)

    github_config = json.dumps(event)
    with open(os.getenv("GITHUB_ENV"), "a") as env_file:
        env_file.write(f"GITHUB_CONFIG={github_config}\n")
