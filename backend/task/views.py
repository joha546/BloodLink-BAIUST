from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, current_user
from ..models import Patient, User
from . import task
from .. import db, login_manager
from .forms import UserProfileForm


@task.route('/edit_profile', methods=['GET', 'POST'])
# @login_required
def edit_profile():
    
    form = UserProfileForm(obj=current_user)

    if form.validate_on_submit():
        current_user.full_name = form.full_name.data
        current_user.baiust_id = form.baiust_id.data
        current_user.blood_group = form.blood_group.data
        current_user.contact_number = form.contact_number.data
        current_user.disease = form.disease.data
        current_user.last_donated = form.last_donated.data
        current_user.hometown = form.hometown.data

        db.session.commit()

        flash('Your profile has been updated!', 'success')
        return redirect(url_for('auth.user_dashboard'))

    return render_template('edit_profile.html', title='Edit Profile', form=form)

from flask_login import  current_user

@task.route('/donation_history')
@login_required
def donation_history():
    # Check if the user is authenticated
    donation_history = current_user.donation_history
    return render_template('donation_history.html', title='Donation History', donation_history=donation_history)



@task.route('/donation_details/<int:patient_id>')
def donation_details(patient_id):
    patient_details = Patient.query.get_or_404(patient_id)
    return render_template('donation_details.html', title='Patient Details', patient_details=patient_details)

