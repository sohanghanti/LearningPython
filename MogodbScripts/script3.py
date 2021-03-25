import json


# def parse_jsonRequest(jsonPath):
#     # print(jsonPath)
#     RequestFilepath = open(jsonPath, 'r')
#     fileContent = RequestFilepath.read()
#     jsonReq = json.loads(fileContent)
#     print(jsonReq)
#     return jsonReq
from datetime import time, datetime, timedelta
from time import sleep

from marshmallow.utils import isoformat

# for i in range(0, 5):
#     # sleep(0.1)
#     # print(datetime.now())
#     # print(datetime.now().isoformat())
#     # print(datetime.strptime("2020-09-17", '%Y-%m-%d').isoformat()[:-3] + 'Z')
#
#     glanceback = timedelta(days=59,
#                            hours=datetime.now().hour,
#                            minutes=datetime.now().minute)
#
#     right_now = datetime.now()
#     # print(right_now - glanceback)
#     print((right_now - glanceback).isoformat()[:-3] + 'Z')
#
# # timestamp = str(datetime.now())
# # timestamp = timestamp.replace("-", "").replace(":", "").replace(" ", "").replace(".", "")
# # print(type(timestamp))


print(datetime.utcnow())
