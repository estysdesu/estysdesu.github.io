from flask import Flask
import os

# init the flask app
estysdesu = Flask(__name__)

# config
estysdesu.config.from_object("flaskApp.config")

# import modules
from flaskApp import models, views
