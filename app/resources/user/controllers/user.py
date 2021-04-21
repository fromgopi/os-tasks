""" User endpoints. """
from flask import Blueprint, request
from app.exceptions.api_exception import ApiError
import json

USER_API = Blueprint('users',__name__)

@USER_API.route('/users', methods=['GET'])
def get_many():
    try:
        users = json.dumps('Welcome to task api')
        
    except ApiError as ex:
        print(ex)