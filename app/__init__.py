from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy  
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config) 
db = SQLAlchemy(app) #db object that represents the db
migrate = Migrate(app, db) #an object that represents the migration engine
login = LoginManager(app) #initialize the Flask-Login
login.login_view = 'login' 


from app import routes, models 