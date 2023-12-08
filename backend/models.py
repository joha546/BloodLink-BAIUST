from backend import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class DonationHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.Float)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    baiust_id = db.Column(db.String(20), unique=True, nullable=False)
    blood_group = db.Column(db.String(3), nullable=False)
    contact_number = db.Column(db.String(15))
    disease = db.Column(db.String(120))
    last_donated = db.Column(db.String(120))
    hometown = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    patient_name = db.Column(db.String(120), nullable=False)
    disease = db.Column(db.String(120), nullable=False)
    blood_group = db.Column(db.String(5), nullable=False)
    baiust_id = db.Column(db.String(255), nullable=False)
    bag_needed= db.Column(db.Integer, nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    request_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Patient('{self.patient_name}', '{self.disease}', '{self.blood_group}')"


class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    last_donation_date = db.Column(db.DateTime)

    def __repr__(self):
        return f"Donor('{self.user.full_name}', '{self.last_donation_date}')"


class UrgentRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    donor_id = db.Column(db.Integer, db.ForeignKey('donor.id'), nullable=True)
    request_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_fulfilled = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"UrgentRequest('{self.patient.patient_name}', '{self.request_date}', '{self.is_fulfilled}')"
    
class BloodPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    number = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    blood_group = db.Column(db.String(255), nullable=False)
    deadline = db.Column(db.String(255), nullable=False)

