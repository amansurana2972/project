from enum import unique
from http.client import ImproperConnectionState
from .import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
  __tablename__='user'
  id=db.Column(db.Integer,primary_key=True)
  username = db.Column(db.String(150), unique=True)
  email=db.Column(db.String,unique=True)
  password=db.Column(db.String)

