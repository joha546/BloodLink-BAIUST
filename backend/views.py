from flask import render_template
from backend import app
from backend.models import User, BloodPost
from flask_login import current_user

@app.route('/')
def index():
    posts = BloodPost.query.all()
    return render_template('index.html', title="Home", posts=posts)


@app.route('/about_us')
def about_us():
    return render_template('about_us.html', title='About Us')
