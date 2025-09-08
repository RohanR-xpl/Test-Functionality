import os
import json

GITHUB_CONFIG = json.loads(os.getenv('GITHUB_CONFIG') or "{}")


print(GITHUB_CONFIG)
print('Sent to Listen')
print('Used Ngrok')
print('success connection')

