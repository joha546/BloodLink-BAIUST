from flask import render_template
from backend import app
from backend.models import User
from flask_login import current_user

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html', title='About Us')
