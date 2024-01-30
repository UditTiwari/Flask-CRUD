from extensions import db
from dataclasses import dataclass
from sqlalchemy.orm import Mapped


@dataclass
class Profile(db.Model):
    id:int
    user_id:int
    bio:str

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    bio = db.Column(db.String(200),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),unique=True)
    user = db.relationship('User',uselist=False,back_populates='profile')

@dataclass
class User(db.Model):
    id:int
    name:str
    profile:Mapped[Profile] 


    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(200),nullable=False)
    profile= db.relationship('Profile',uselist=False,back_populates='user')
