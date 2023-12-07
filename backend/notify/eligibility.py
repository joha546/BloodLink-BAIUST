from flask import flash, redirect, url_for
from flask_login import login_required, current_user
from backend import app, db
from ..models import Donor
from datetime import datetime, timedelta

def check_donation_eligibility():
    donor = Donor.query.filter_by(user_id=current_user.id).first()


    if donor.last_donation_date is None or (datetime.utcnow() - donor.last_donation_date) >= timedelta(days=90):
        flash('You are eligible to donate blood!', 'success')
    else:
            flash('You must wait at least 3 months between donations.', 'danger')
            
