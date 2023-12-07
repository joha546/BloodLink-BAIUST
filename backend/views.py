from flask import render_template
from backend import app
from backend.models import User

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/about_us')
def about_us():
    return render_template('about_us.html', title='About Us')
