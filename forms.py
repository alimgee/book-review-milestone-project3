from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, \
    TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(),
                           Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Register Now')


class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(),
                           Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in Now')


class ReviewForm(FlaskForm):

    author = StringField('Author', validators=[DataRequired(),
                         Length(min=2, max=80)])
    book_title = StringField('Book Title', validators=[DataRequired(),
                             Length(min=1, max=150)])
    summary = TextAreaField('Book Bite Summary (200 char)',
                            validators=[DataRequired(), Length(min=2,
                                        max=200)])
    review = TextAreaField('Book Bite Review (1500 char)',
                           validators=[DataRequired(), Length(min=2,
                                       max=1500)])
    category = SelectField(u'Genre', choices=[
        ('factual', 'Fact'),
        ('fiction', 'Fiction'),
        ('health', 'Health'),
        ('nature', 'Nature'),
        ('science', 'Science'),
        ('sport', 'Sport'),
        ('history', 'World History'),
        ])
    submit_add = SubmitField('Add Review')
    submit_edit = SubmitField('Update Review')