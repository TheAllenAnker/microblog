#Author: Allen Anker
#Created by Fenyr_Allen on 22/05/2018

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes