import json
import requests
import jsonpath

url = "https://www.thetestingworldapi.com/api/StDetails/1104"
data = {'grant_type': 'password', 'username': 'admin', 'password': ''}

token_url = "https://www.thetestingworldapi.com/Token"
token = requests.post(token_url, data)
json_token = json.loads(token.text)
token_value = jsonpath.jsonpath(token.text, 'access_token')

auth = {'Authorization': 'Bearer' + token_value[0]}

res = requests.get(url, headers=auth)
print(res.text)
