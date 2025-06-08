from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    middlename = StringField('Middle Name')
    lastname = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    contact_number = StringField('Contact Number', validators=[DataRequired()])
    address = StringField('Street Address', validators=[DataRequired()])
    submit = SubmitField('Register')
