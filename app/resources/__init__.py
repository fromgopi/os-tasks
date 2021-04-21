#pylint: disable=import-error, missing-final-newline,trailing-whitespace,trailing-newlines,no-member
""" Listing all the routes"""
from .users import UsersResource

def initialize_routes(api):
    """
    Initialize the routes 

    Args:
        api ([Flask restful]): [Flask restful object]
    """
    api.add_resource(UsersResource, '/api/users')