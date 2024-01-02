from flask import Blueprint

from .database

blog = Blueprint('blog',__name__,template_folder='templates')

from blog import routes