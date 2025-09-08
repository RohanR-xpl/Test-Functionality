import os
import json

event_path = os.getenv('GITHUB_EVENT_PATH')
print('---------------')
print(event_path)
print(os.path.exists(event_path))
print('---------------')
if event_path and os.path.exists(event_path):
    event = {}
    with open(event_path, 'r') as f:
        # event = json.dumps(f)
        print(event)
    os.environ['GITHUB_CONFIG'] = event or ''
    print('out')
