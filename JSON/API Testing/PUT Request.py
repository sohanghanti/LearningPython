import json
import jsonpath
import requests

url = 'https://reqres.in/api/users/2'
file = open(r'C:\pyCharmProjects\learningPython\JSON\API Testing\putReq.json','r')
req = file.read()
json_req = json.loads(req)

response = requests.put(url, json_req)
print(response.text)
print(response.status_code)
print(response.headers)
print(response.content)

json_response = json.loads(response.text)
name = jsonpath.jsonpath(json_response, 'name')
print(name[0])
updatedAt = jsonpath.jsonpath(json_response, 'updatedAt')
print(updatedAt[0])