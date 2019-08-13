from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username' , validators =[DataRequired() , Length(min=3, max =20)])
    password = PasswordField('Password' , validators =[DataRequired()])
    confirm_password = PasswordField('Confirm Password' , validators =[DataRequired() , EqualTo('password')])
    submit = SubmitField('Register Now')

class LoginForm(FlaskForm):
    username = StringField('Username' , validators =[DataRequired() , Length(min=3, max =20)])
    password = PasswordField('Password' , validators =[DataRequired()])
    submit = SubmitField('Log in Now')