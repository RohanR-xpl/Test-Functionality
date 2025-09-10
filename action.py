import os
import json
import logging
import sys

GITHUB_EVENT_PATH = os.getenv('GITHUB_EVENT_PATH')
event = {}

if GITHUB_EVENT_PATH and os.path.exists(GITHUB_EVENT_PATH):
    with open(GITHUB_EVENT_PATH, 'r') as f:
        event = json.load(f) or {}


if not event:
    logging.error('FAILED : Could not find github event path')
    sys.exit(1)

print(event)