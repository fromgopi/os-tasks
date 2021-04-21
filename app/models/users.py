#pylint: disable=missing-final-newline,invalid-name,trailing-whitespace
"""user Model"""
from app.db.database import Database

class Users():
    """
    User Model extending Mongodb Document

    Args:
        DB (Mongoengine): Mongoengine document 
    """
    def __init__(self):
        self.db = Database()
        self.collection_name = 'users'

    
    
    