from flask import flash

from backend import db
from backend.task.forms import RegistrationForm, UserProfileForm
from flask import request
from backend.models import User
from backend.task.forms import LoginForm
from flask import redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user
from . import auth
from .. import login_manager


# Load user callback for Flask-Login
# Load user callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.user_dashboard'))

    if request.method == 'POST':
        email = request.form.get('email')  # Change 'username' to 'email'
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()  # Change 'username' to 'email'

        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!', 'success')

            # Redirect to user_dashboard
            return redirect(url_for('auth.user_dashboard'))
        else:
            flash('Login unsuccessful. Please check your email and password.', 'danger')

    return render_template('login.html', title='Login Page')


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

    form = RegistrationForm()

    if form.validate_on_submit():
        new_user = User(
            full_name=form.full_name.data,
            baiust_id=form.baiust_id.data,
            blood_group=form.blood_group.data,
            contact_number=form.contact_number.data,
            disease=form.disease.data,
            last_donated=form.last_donated.data,
            hometown=form.hometown.data,
            email=form.email.data
        )

        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()

        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for("auth.login"))

    return render_template('signup.html', title='Register', form=form)

# User Profile Dashboard route
@auth.route('/user_dashboard')
#@login_required
def user_dashboard():
    return render_template('user_dashboard.html', title='User Dashboard')