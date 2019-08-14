from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
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

class AddReviewForm(FlaskForm):
    author = StringField('Author' , validators =[DataRequired() , Length(min=2, max =40)])
    book = StringField('Book Title' , validators =[DataRequired() , Length(min=1, max =50)])
    summary = TextAreaField('Book Bite Summary (200 char)' , validators =[DataRequired() , Length(min=2, max =200)])
    review = TextAreaField('Book Bite Review (1500 char)' , validators =[DataRequired() , Length(min=2, max =1500)])
    genre = SelectField(u'Genre', choices=[ ('fa fa-picture-o', 'Fact'), ('fa fa-picture-o', 'Fiction'), ('fa fa-heartbeat', 'Health'),
    ('fa fa-leaf', 'Nature'), ('fa fa-cogs', 'Science'),('fa fa-futbol-o', 'Sport'), ('fa fa-globe', 'World History')  ])
    submit = SubmitField('Add review')