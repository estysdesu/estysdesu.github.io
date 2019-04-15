from flask import Flask
import os

# init the flask app
mySiteApp = Flask(__name__, instance_relative_config=True)

# config
mySiteApp.config.from_object("config")
if os.path.exists("instance"):
    mySiteApp.config.from_pyfile("config.py")

# import modules
from . import models, views
