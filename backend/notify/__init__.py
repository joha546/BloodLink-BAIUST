from flask import Blueprint

notify = Blueprint('notify', __name__, template_folder='templates')

from . import views