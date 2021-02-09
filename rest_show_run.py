import requests
import json
r = requests.get("https://{}/restconf{}".format('10.204.10.13', '/data?content=config'), auth=('admin', 'admin'), verify=False)
with open('pd99-esp-001.json', 'w') as json_file:
    json.dump(r.json(), json_file, indent=4)