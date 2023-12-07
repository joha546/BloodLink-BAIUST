from flask import flash
from .. import db
from backend.task.forms import RegistrationForm, UserProfileForm
from flask import request
from ..models import User
from backend.task.forms import LoginForm
from flask import redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user
from . import auth
from .. import login_manager


# Load user callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/login')
def login():
    return render_template('login.html', title='Login Page')

# Login route
@auth.route('/login', methods=['GET', 'POST'])
def login_post():
    if current_user.is_authenticated:
        return redirect(url_for('auth.user_dashboard'))

    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first()

    if not user or not user.password_hash == password:
        login_user(user, remember=True)
        return redirect('auth.login')

    return redirect(url_for('auth.user_dashboard'))


# Logout route
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

# Registration route
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.user_dashboard'))

    if request.method == 'POST':
        full_name=request.form['full_name']
        baiust_id=request.form['baiust_id']
        blood_group=request.form['blood_group']
        contact_number=request.form['contact_number']
        disease=request.form['disease']
        last_donated=request.form['last_donated']
        hometown=request.form['hometown']
        email=request.form['email']
        password_hash = request.form['password']

        new_user = User(
            full_name=full_name,
            baiust_id=baiust_id,
            blood_group=blood_group,
            contact_number=contact_number,
            disease=disease,
            last_donated=last_donated,
            hometown=hometown,
            email=email,
            password_hash=password_hash
        )

        db.session.add(new_user)
        db.session.commit()

        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for("auth.login"))

    return render_template('signup.html', title='Register')

# User Profile Dashboard route
@auth.route('/user_dashboard')
#@login_required
def user_dashboard():
    return render_template('user_dashboard.html', title='User Dashboard')