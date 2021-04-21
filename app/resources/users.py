#pylint: disable=import-error, missing-final-newline,trailing-whitespace,trailing-newlines,no-member
""" User controller """
from flask import request, Response
from flask_restful import Resource
import json
from app.exceptions.api_exception import ApiError 
from app.utils import response

class UsersResource(Resource):
    """
    User controller

    Args:
        Resource ([Flask_Restful]): flask restful resource
    """
    def get(self):
        users = json.dumps('Welcome to Task api')
        
        return Response(users, mimetype='application/json', status=200)
    
    def post(self):
        try:
            if request.headers.get('Content-Type') == 'application/json':
                json_data = request.json
                print(json_data)
                return Response('ok', mimetype='application/json', status=200)
            
        except KeyError as ex:
            print(ex)
            return response.error(ex)