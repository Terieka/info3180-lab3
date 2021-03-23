
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField,validators 
from wtforms.validators import DataRequired, Email
  
class ContactForm(FlaskForm):
    name = TextField('Name', [validators.Required('Please enter your name')])
    email = TextField('Email', [validators.Required('An email address is required!') ])
    subject = TextField('Subject',[ validators.Required('A subject is required!')])
    message = TextAreaField('Message', [validators.Required('A message is required!')])
    submit = SubmitField ('Send')