
from flask import Blueprint
from flask_restful import Api
from api.resources.users import UserList


blueprint = Blueprint('api',__name__)
api = Api(blueprint,errors=blueprint.errorhandler)

api.add_resource(UserList,'/users')