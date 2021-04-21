#pylint: disable=missing-final-newline,unused-import,trailing-whitespace,too-few-public-methods,invalid-name,undefined-variable
""" Pymongo class db"""
import os
from datetime import datetime
from pymongo import MongoClient

class Database():
    """
    Database class

    Args:
        object ([type]): [description]
    """
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGODB_URL'))
        self.db = self.client[os.getenv('MONGODB_DB')]
    

    def inser(self, data, collection_name):
        """
        Generic Insert method

        Args:
            data ([JSON Data]): JSon Data
            collection_name ([Str]): Collection Name
        """
        data['created_on'] = datetime.now()
        data['updated_on'] = datetime.now()
        result = self.db[collection_name].insert_one(data)
        return str(result.inserted_id)