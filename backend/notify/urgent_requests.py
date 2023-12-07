from flask import render_template, flash, redirect, url_for
from flask_mail import Message
from backend import app, db, mail
from ..models import Patient, Donor
from flask_login import login_required, current_user
from .eligibility import check_donation_eligibility

@app.route('/urgent_requests', methods=['GET', 'POST'])
#@login_required
def submit_urgent_requests():
    patients = Patient.query.filter_by(is_urgent=True).all()

    for patient in patients:
        donors = Donor.query.filter_by(blood_group=patient.blood_group).all()


        for donor in donors:
            # Check if donor's blood group matches patient's blood group
            if donor.user.blood_group == patient.blood_group:
                if check_donation_eligibility(donor.user):  # Check eligibility before sending SMS
                    send_sms_to_donor(patient, donor.user)

    flash('Urgent SMS notifications sent to potential donors!', 'success')
    return redirect(url_for('auth.user_dashboard'))

def send_sms_to_donor(patient, donor_user):
    # Customize this function based on your SMS content and configuration
    # Send SMS using a third-party SMS gateway or service
    # Example: SMS gateway API integration or use a service like Twilio

    # SMS content could be like:
    # sms_content = f"Urgent blood donation request! Patient ({patient.patient_name}) needs blood. Contact hospital for details."

    # Code for sending SMS goes here
    # Example: Sending SMS using Flask-Mail for demonstration purposes
    send_sms_via_mail(patient, donor_user)

def send_sms_via_mail(patient, donor_user):
    # Example: Sending SMS-like message using Flask-Mail
    subject = f"Urgent Blood Donation Request"
    body = f"Urgent blood donation request! Patient ({patient.patient_name}) needs blood. Contact hospital for details."

    message = Message(subject, recipients=[donor_user.email], body=body)
    mail.send(message)
