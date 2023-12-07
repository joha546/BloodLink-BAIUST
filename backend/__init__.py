from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.app_context().push()
login_manager = LoginManager(app)
migrate = Migrate(app, db)
mail = Mail(app)

from .task import task as task_blueprint
app.register_blueprint(task_blueprint)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .notify import notify as notify_blueprint
app.register_blueprint(notify_blueprint)

from backend import views, models
