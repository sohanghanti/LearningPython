import json
import requests
import jsonpath

baseUrl = 'https://reqres.in'
req = '/api/users?page=2'
payload = {'abc':'123'}

response = requests.get(baseUrl + req, params=payload)
print(response)
print(response.headers)
print('###################################')
print(response.status_code)
print(response.content)


# HEADER Content
print(response.headers.get('Date'))
print('################################')
print(response.headers.get('Server'))
print('################################')

# Cookies, Encoding, Elapsed Time etc.
print(response.cookies)
print('################################')
print(response.encoding)
print('################################')
print(response.elapsed)

# any specific value from the response content
json_resp = json.loads(response.text)

resp = jsonpath.jsonpath(json_resp, 'data')
print(resp)
resp = jsonpath.jsonpath(json_resp, 'data[0]')
print(resp)
id = jsonpath.jsonpath(json_resp, 'data[0].id')
print(id)


# print all the Id's
print(len(resp[0]))


for i in range(0, len(resp[0])):
    resp = jsonpath.jsonpath(json_resp, 'data' + '[' + str(i) + ']' + '.id')
    print(resp)


