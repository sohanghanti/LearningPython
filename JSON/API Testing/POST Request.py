import json
import jsonpath
import requests

url = 'https://reqres.in/api/users'
file = open(r'C:\pyCharmProjects\learningPython\JSON\API Testing\postReq.json', 'r')
fileContent = file.read()

json_content = json.loads(fileContent)
print(json_content)
response = requests.post(url, json_content)
print(response.text)
print(response.status_code)
print(response.headers)


json_response = json.loads(response.text)
print(jsonpath.jsonpath(json_response, 'id'))
id = jsonpath.jsonpath(json_response, 'id')
print(id[0])

