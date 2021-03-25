import json
from JSON.testClass import Laptop

laptop1 = Laptop()
jsonStr = json.dumps(laptop1.__dict__)

# print json string
print(jsonStr)
