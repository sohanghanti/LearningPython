import json
import requests
import jsonpath

parameters = {'name': 'testingworld', 'email' : 'testingworldindia@gmail.com'}
url = 'https://httpbin.org/get'
response = requests.get(url, params=parameters)
print(response.status_code)
print(response.text)

response_json = json.loads(response.text)
print(response_json)