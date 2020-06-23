# send request to API
#  parse response into Json
# validate data by json path

# sample API: https://reqres.in/api/users?page=2


import requests
import json
import jsonpath

api_url = 'https://reqres.in/api/users?page=2'

# make a request
response1 = requests.get(api_url)

# validate response and status code
print(response1.text)
print(response1.status_code)
assert response1.status_code == 200

# parse response into json format
json_response = json.loads(response1.text)
print(json_response)

# validate response by using jsonpath
# fetch the data using jsonpath module

x = jsonpath.jsonpath(json_response, 'total')  # apply json path
print(x)

y = jsonpath.jsonpath(json_response, 'data[0].first_name')
print(y)
print(y[0])

