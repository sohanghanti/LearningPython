from datetime import datetime

from bson import ObjectId
from pymongo import MongoClient
from pprint import pprint


class Connect:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def connect(self):
        client = MongoClient(
            "mongodb+srv://" + self.username + ":" + self.password + "@d-rnd-db-paris-zd9nu.azure.mongodb.net/" + self.username + "-cyberproof "
                                                                                                                                  "?retryWrites=true")

        list_of_db = client.list_database_names()
        for i in list_of_db:
            if str(i) == self.username + '-cyberproof':
                dbname = i
                break

        db = client[self.username]
        return db

    def getCollection(self, collection_name):
        db = self.connect()
        collection = db[collection_name]
        return collection_name




