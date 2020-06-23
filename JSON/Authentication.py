import json

import jsonpath
import requests
from requests.auth import HTTPBasicAuth

url = "https://developer.github.com/v3/users/#get-the-authenticated-user"
res = requests.get(url, auth=HTTPBasicAuth('sohan.ghanti@gmail.com', 'Welcome1@3$'))
print(res.status_code)
print(res.text)

json_res = json.loads(res.text)
print(jsonpath.jsonpath(json_res, 'id'))
print(jsonpath.jsonpath(json_res, 'login'))

