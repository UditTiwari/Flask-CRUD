from flask_restful import Resource
from flask import request ,jsonify
from models.user import User ,Profile
from extensions import db

class UserList(Resource):


    def get(self):
        user = User.query.all
        return jsonify(msg=user)
    

    def post(self):
        data = request.json
        profile_data = data.get("profile")  # Assuming profile data is nested in the request JSON

        # Create a new Profile object
        profile = Profile(
            bio=profile_data.get("bio"),
            # Add other profile attributes here
        )

        # Create a new User object and assign the profile
        user = User(
            name=data.get("name"),
            profile=profile  # Assign the profile object to the user's profile attribute
        )
        # user = User(name='Test User')
        # profile = Profile(bio='Test user profile')

        # user.profile = profile
        db.session.add(user)
        db.session.commit()

        return {"message": 'Username added'},200

