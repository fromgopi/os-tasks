#pylint: disable=import-error,unused-import
""" User endpoints. """
from flask import Blueprint, request,Response
import json
from app.exceptions.api_exception import ApiError
from app.resources.user.services.user import UserService


USER_API = Blueprint('users',__name__)

@USER_API.route('/users', methods=['GET'])
def get_many():
    """ Get Many Controller """
    try:
        users = json.dumps('Welcome to task api')
        UserService().get_many()
        return Response(users, mimetype='application/json', status=200)
    except ApiError as ex:
        print(ex)