from flask_restful import Resource
from flask import request ,jsonify
from models.user import User ,Profile
from extensions import db

class ProfileRegister(Resource):
    def get(self):
        user = Profile.query.all()

        return jsonify(msg="Users",user=user)
    



class ProfileList(Resource):

    def get(self,user_id):
        profile = Profile.query.get_or_404(user_id)
        user = User.query.get(profile.user_id)


        return jsonify(
            profile_data={
                "id": profile.id,
                "bio": profile.bio
            },
            username=user.name
        )

