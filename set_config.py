import os
import json

event_path = os.getenv('GITHUB_EVENT_PATH')

if event_path and os.path.exists(event_path):
    with open(event_path, 'r') as f:
        event = json.load(f)
    os.environ['GITHUB_CONFIG'] = event or {}
    
    