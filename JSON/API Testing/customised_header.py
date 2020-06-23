import json, requests, jsonpath

header_data_dict = {'T1': 'first header', 'T2': 'second header'}
response = requests.get('https://httpbin.org/get', headers=header_data_dict)
print(response.text)
