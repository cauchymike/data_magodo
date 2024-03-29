from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
import os
from flask_sqlalchemy import SQLAlchemy
from os import environ, path
import pymysql
from dotenv import load_dotenv




app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

#configurations for our app
app.config['FLASK_APP']= environ.get('FLASK_APP')
app.config['SECRET_KEY']= environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']= environ.get('CLEARDB_DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
app.config['DEBUG']=environ.get('DEBUG')
app.config['FLASK_ENV'] = environ.get('FLASK_ENV')




############################
### DATABASE SETUP ##########
#############################

db = SQLAlchemy(app)
Migrate(app,db)


#########################
# LOGIN CONFIGS
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'




from magodo_app.core.views import core
from magodo_app.users.views import users
from magodo_app.errorpages.handlers import error_pages

#we use blueprint to connect all our views together
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)



