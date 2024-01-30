from extensions import db
from dataclasses import dataclass


class User(db.Model):
    
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(200),nullable=False)
    profile= db.relationship('Profile',uselist=False,back_populates='user')


class Profile(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    bio = db.Column(db.String(200),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),unique=True)
    user = db.relationship('User',uselist=False,back_populates='profile')