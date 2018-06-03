# Author: Allen Anker
# Created by Fenyr_Allen on 22/05/2018

from app import app, db
from app.models import User, Post
from app import cli


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
