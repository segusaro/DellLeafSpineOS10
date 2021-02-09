import requests
import json
from pprint import pprint as pp

with open('interface.json', 'r') as file:
    payload = json.load(file)

r = requests.patch("https://{}/restconf{}".format('10.204.10.13', '/data/ietf-interfaces:interfaces'), json=payload, auth=('admin', 'admin'), verify=False)
r = requests.get("https://{}/restconf{}".format('10.204.10.13', '/data/ietf-interfaces:interfaces/interface=ethernet1%2F1%2F5?content=config'), auth=('admin', 'admin'), verify=False)
pp(r.json())
