import datetime
from flask import render_template, flash, redirect, request, url_for
from flask_login import login_required, current_user
from wtforms import StringField
from backend import app, db, mail
from . import notify 
from backend.models import Patient, Donor,DonationHistory
from flask_mail import Message  
from .eligibility import check_donation_eligibility
from .urgent_requests import send_sms_to_donor, submit_urgent_requests 
from ..task.forms import PatientForm


@notify.route('/blood_request_form', methods=['GET', 'POST'])
# @login_required
def blood_request_form():
    form = PatientForm()  # Create an instance of the PatientForm

    if form.validate_on_submit():
        # Process the blood request form submission
        patient_name = form.patient_name.data
        disease = form.disease.data
        blood_group = form.blood_group.data
        address = form.address.data
        bag_needed = form.bag_needed.data
        baiust_id = form.baiust_id.data
        contact_number = form.contact_number.data
        email = form.email.data

        # Create a new patient entry
        new_patient = Patient(
            user_id=current_user.id if current_user.is_authenticated else None,
            patient_name=patient_name,
            disease=disease,
            blood_group=blood_group,
            address=address,
            bag_needed=bag_needed,
            baiust_id=baiust_id,
            contact_number=contact_number,
            email=email
        )

        db.session.add(new_patient)
        db.session.commit()

        # Send notifications to potential donors
        send_notifications(new_patient)

        flash('Blood request submitted successfully! Notifications sent to potential donors.', 'success')
        return redirect(url_for('auth.user_dashboard'))

    return render_template('blood_req_form.html', title='Blood Request Form', form=form)

# Include the route for submitting urgent blood requests from urgent_requests.py
notify.add_url_rule('/urgent_blood_request', 'submit_urgent_request', submit_urgent_requests, methods=['POST'])

@notify.route('/donation')
# @login_required
def donation():
    blood_requests = Patient.query.all()
    return render_template('donation_list.html', title='Blood Donation List', blood_requests=blood_requests)



@notify.route('/accept_request/<int:request_id>', methods=['POST'])
@login_required
def accept_request(request_id):
    blood_request = Patient.query.get_or_404(request_id)
    
    donor = Donor.query.filter_by(user_id=current_user.id).first()

    if donor:
        donor.last_donation_date = datetime.utcnow()
        
        # Create or update DonationHistory for the user
        donation_history = DonationHistory.query.filter_by(user_id=current_user.id).first()

        if donation_history:
            # If the user already has a donation history, update it
            donation_history.amount += 1 
            donation_history.date = datetime.utcnow()
        else:
            # If the user doesn't have a donation history, create a new one
            donation_history = DonationHistory(user_id=current_user.id, amount=1, date=datetime.utcnow())

        db.session.add(donation_history)
        db.session.commit()


        blood_request.donor_name = donor.user.full_name
        blood_request.donor_uid = donor.user.uid
        blood_request.donor_blood_group = donor.user.blood_group
        blood_request.donor_contact_number = donor.user.contact_number
        blood_request.donor_email = donor.user.email

        db.session.commit()

        flash('Blood request accepted! Thank you for your donation.', 'success')
        return redirect(url_for('auth.user_dashboard'))
    else:
        flash('You are not registered as a donor. Please contact the admin.', 'danger')
        return redirect(url_for('notify.donation'))




@notify.route('/reject_request/<int:request_id>', methods=['POST'])
# @login_required
def reject_request(request_id):
    blood_request = Patient.query.get_or_404(request_id)

    # Check if the blood request has already been accepted
    if blood_request.is_accepted:
        flash('This blood request has already been accepted. You cannot reject it.', 'warning')
        return redirect(url_for('notify.donation'))

    
    if blood_request.is_rejected:
        flash('This blood request has already been rejected.', 'warning')
        return redirect(url_for('notify.donatoin'))

    blood_request.is_rejected = True
    db.session.commit()

    flash('Blood request rejected!', 'info')
    return redirect(url_for('auth.user_dashboard'))



def send_notifications(patient):
    donors = Donor.query.all()

    for donor in donors:
        # Check if donor's blood group matches patient's blood group
        if donor.user.blood_group == patient.blood_group:
            # Check eligibility before sending email
            if check_donation_eligibility(donor.user):
                send_email_to_donor(patient, donor.user)

            # Check eligibility before sending urgent SMS
            if patient.is_urgent and check_donation_eligibility(donor.user):
                send_sms_to_donor(patient, donor.user)

def send_email_to_donor(patient, donor_user):
    # Customize this function based on your email content and configuration
    msg = Message('Blood Donation Request',
                  sender='noreply@example.com',
                  recipients=[donor_user.email])
    msg.body = f"Dear {donor_user.full_name},\n\nA patient in need ({patient.patient_name}) is requesting blood. Please consider donating if you are eligible.\n\nBest regards,\nThe Blood Donation Team"
    
    with app.app_context():
        mail.send(msg)
        
        