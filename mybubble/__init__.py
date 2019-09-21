from flask import Flask
from mybubble.registration_form import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "ce3d6168915c2a48dcee679cbe2ac49a"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)

from mybubble import routes
