from flask import Flask

# init the flask app
mySiteApp = Flask(__name__, instance_relative_config=True)

# config
mySiteApp.config.from_object("config")
mySiteApp.config.from_pyfile("config.py")

# import modules
from . import models, views
