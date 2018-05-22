#Author: Allen Anker
#Created by Fenyr_Allen on 22/05/2018

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'