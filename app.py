import os
import json
import logging

logging.basicConfig(level=logging.DEBUG)

logging.info('------ Github Action Execution Started -------')

GITHUB_EVENT_PATH = os.getenv('GITHUB_EVENT_PATH')

event = {}

if GITHUB_EVENT_PATH and os.path.exists(GITHUB_EVENT_PATH):
    with open(GITHUB_EVENT_PATH, 'r') as f:
        event = json.load(f)
        event = event if event else {}
        
    
        
        
logging.info('------ Github Action Execution Ended -------')

