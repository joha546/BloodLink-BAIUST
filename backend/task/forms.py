from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, SubmitField, DateField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = SubmitField('Remember Me')


class RegistrationForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    baiust_id = StringField('BAIUST ID', validators=[DataRequired()])
    blood_group = StringField('Blood Group', validators=[DataRequired()])
    contact_number = StringField('Contact Number', validators=[DataRequired()])
    disease = StringField('Disease (if any)')
    last_donated = DateField('Last Donated (YYYY-MM-DD)', format='%Y-%m-%d')
    hometown = TextAreaField('Hometown', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

class PatientForm(FlaskForm):
    patient_name = StringField('Patient Name', validators=[DataRequired(), Length(max=120)])
    disease = StringField('Disease', validators=[Length(max=120)])
    blood_group = SelectField('Blood Group', choices=[('A+', 'A-'), ('B+', 'B-'), ('AB+', 'AB-'), ('O+', 'O-')], validators=[DataRequired()])
    address = TextAreaField('Address', validators=[DataRequired(), Length(max=255)])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    baiust_id = StringField('BAIUST ID', validators=[DataRequired()])
    
    submit = SubmitField('Submit')


class UserProfileForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired(), Length(max=100)])
    baiust_id = StringField('BAIUST ID', validators=[DataRequired(), Length(max=20)])
    blood_group = SelectField('Blood Group', choices=[
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')
    ], validators=[DataRequired()])
    contact_number = StringField('Contact Number', validators=[DataRequired(), Length(min=11, max=15)])
    disease = StringField('Disease', validators=[Length(max=255)])
    last_donated = DateField('Last Donated', format='%Y-%m-%d')
    address = StringField('Hometown', validators=[Length(max=255)])
    submit = SubmitField('Save Changes')
    
    