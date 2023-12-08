import os
from flask import render_template, redirect, url_for, request
from flask_login import login_required
from flask_mail import Message

from ..models import User, BloodPost
from . import task
from .. import db, mail

mail_user = os.environ.get('MAIL_USERNAME')


'''@task.route('/edit_profile', methods=['GET', 'POST'])
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

'''
@task.route('/create_post', methods=['GET', 'POST'])
def create_post():
    #user_emails = [user.email for user in User.query.filter_by(blood_group="B+").all()]

    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        number = request.form['number']
        email = request.form['email']
        blood_group = request.form['blood_group']
        bag_needed = request.form['bag_needed']
        deadline = request.form['deadline']

        new_post = BloodPost(
            name=name,
            address=address,
            number=number,
            email=email,
            blood_group=blood_group,
            bag_needed=bag_needed,
            deadline=deadline
        )

        db.session.add(new_post)
        db.session.commit()

        user_emails = [user.email for user in User.query.filter_by(blood_group=blood_group).all()]

        msg = Message(f'{request.form.get("name")} needs blood', sender=('BloodLink BAIUST', mail_user), recipients=user_emails)
        msg.body = f"{request.form.get('name')} needs {request.form.get('blood_group')} blood from BloodLink BAIUST."
        mail.send(msg)

        return redirect(url_for('index'))

        
    return render_template('blood_post.html', title="Create Post")

@task.route('/view_post/<int:id>', methods=['POST', 'GET'])
@login_required
def view_post(id):
    post = BloodPost.query.get_or_404(id)
    
    if request.method == 'POST':   
        msg = Message(f'{request.form.get("name")} agreed to give blood', sender=('BloodLink BAIUST','heavenoncrack@gmail.com'), recipients=[post.email])

        msg.body = f"""{request.form.get('name')} has accepted your blood request from BloodLink BAIUST.
Contact Number: {request.form.get('number')}"""
        
        mail.send(msg)
        bags = post.bag_recieved + 1
        if post.bag_recieved == post.bag_needed - 1:
            post.donated = True

        post.bag_recieved = bags
        db.session.commit()

        return redirect(url_for('task.accept'))

    return render_template('post.html', post=post)

@task.route('/accept')
@login_required
def accept():
    return "<h1>Success!!!</h1>"
