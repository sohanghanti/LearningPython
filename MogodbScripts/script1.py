from datetime import datetime

from bson import ObjectId
from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://qa-10:8qenDKl4mPHmN6t2@d-rnd-db-paris-zd9nu.azure.mongodb.net/qa-10-cyberproof"
                     "?retryWrites=true")

list_of_db = client.list_database_names()
dbname = ''
for i in list_of_db:
    if str(i) == 'qa-10-cyberproof':
        print("exists")
        dbname = i
        break

mydb = client[dbname]

'-------------------------------------'
collection = mydb['incidents']
'-------------------------------------'

# print(collection.find_one())

# print(collection)


record = [{
    "_id": ObjectId(),
    "summary": {
        "survey": []
    },
    "status": 20,
    "type": "Malware",
    "alerts": [],
    "observables": [],
    "users": [],
    "tags": [],
    "source": "manual",
    "name": "anyIncident5",
    "description": "anyIncident5",
    "priority": {
        "value": "Medium",
        "color": "#ffab00",
        "order": 1
    },
    "organization": ObjectId("5f3659f85ed39200175103e1"),
    "severity": "Medium",
    "modifiedBy": ObjectId("5f3a87bda30eb10018022ac1"),
    "createdBy": ObjectId("5f3a87bda30eb10018022ac1"),
    "group": "L2",
    "ownerRef": {
        "_id": ObjectId("5f3a87bda30eb10018022ac1"),
        "displayName": "System Admin"
    },
    "playbooks": [],
    "external": [],
    "created": datetime.now().isoformat()[:-3]+'Z',
    "modified": datetime.now().isoformat()[:-3]+'Z',
    "edges": [],
    "evidences":
        [
            {
                "name": "Incident created",
                "description": "Incident created by System Admin",
                "data": {
                    "user": ObjectId("5f3a87bda30eb10018022ac1")
                },
                "type": "Incident created",
                "created": datetime.now().isoformat()[:-3]+'Z',
                "reported": datetime.now().isoformat()[:-3]+'Z'
            }
        ],
    "key": "CDC-20200914-00004",
    "__v": 1
},
    {
        "_id": ObjectId(),
        "summary": {
            "survey": []
        },
        "status": 20,
        "type": "Malware",
        "alerts": [],
        "observables": [],
        "users": [],
        "tags": [],
        "source": "manual",
        "name": "anyIncident5",
        "description": "anyIncident5",
        "priority": {
            "value": "Medium",
            "color": "#ffab00",
            "order": 1
        },
        "organization": ObjectId("5f3659f85ed39200175103e1"),
        "severity": "Medium",
        "modifiedBy": ObjectId("5f3a87bda30eb10018022ac1"),
        "createdBy": ObjectId("5f3a87bda30eb10018022ac1"),
        "group": "L2",
        "ownerRef": {
            "_id": ObjectId("5f3a87bda30eb10018022ac1"),
            "displayName": "System Admin"
        },
        "playbooks": [],
        "external": [],
        "created": datetime.now().isoformat()[:-3] + 'Z',
        "modified": datetime.now().isoformat()[:-3] + 'Z',
        "edges": [],
        "evidences":
            [
                {
                    "name": "Incident created",
                    "description": "Incident created by System Admin",
                    "data": {
                        "user": ObjectId("5f3a87bda30eb10018022ac1")
                    },
                    "type": "Incident created",
                    "created": datetime.now().isoformat()[:-3] + 'Z',
                    "reported": datetime.now().isoformat()[:-3] + 'Z'
                }
            ],
        "key": "CDC-20200914-00005",
        "__v": 1
    }
]

# print(datetime.now().isoformat()[:-3]+'Z')
# collection.insert_many(record)


jsonPath = ''
data = ''
var = 'incidents'
if var == 'incidents':
    jsonPath = '..\\db\\db_templates\\insert_incident.json'

print(jsonPath)