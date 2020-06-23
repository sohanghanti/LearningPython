import json
import jsonpath
import requests

url = 'https://reqres.in/api/users/2'

response = requests.delete(url)
print(response)
print(response.text)
print(response.status_code)
print(response.content)

# json_response = json.loads(response.text)
# print(jsonpath.jsonpath(json_response, 'data'))
# print(jsonpath.jsonpath(json_response, 'data[id]'))
