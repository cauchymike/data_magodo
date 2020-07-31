from magodo_app import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    full_name = db.Column(db.String(70), nullable = False)
    password_hash = db.Column(db.String(128), nullable = False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    phone_number = db.Column(db.String(64), unique = True, index = True)
    house_describe = db.Column(db.String(500), nullable = False)#if you want it to be unique, then you give it an index
    house_number = db.Column(db.Integer, nullable = False)
    street_name = db.Column(db.String(30), nullable = False)
    house_type = db.Column(db.String(30), nullable = False)




    def __init__(self,email,username,password, phone_number, house_describe,
                 house_number, full_name, street_name, house_type):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.phone_number = phone_number
        self.house_describe = house_describe
        self.house_number = house_number
        self.full_name = full_name
        self.street_name = street_name
        self.house_type = house_type



    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Full name: {self.username}, with  Phone Number: {self.phone_number}, Living at: {self.street_name}," \
               f"number: {self.house_number}, building type is {self.house_type}"
