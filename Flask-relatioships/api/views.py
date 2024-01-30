
from flask import Blueprint
from flask_restful import Api
from api.resources.users import UserRegister,UserList
from api.resources.profiles import ProfileRegister,ProfileList


blueprint = Blueprint('api',__name__)
api = Api(blueprint,errors=blueprint.errorhandler)

api.add_resource(UserRegister,'/users')
api.add_resource(UserList,'/users/<int:user_id>')
api.add_resource(ProfileRegister,'/userprofile')
api.add_resource(ProfileList,'/userprofile/<int:user_id>')
