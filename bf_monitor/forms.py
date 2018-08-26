from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectMultipleField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from bf_monitor.models.user import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        if User.find_by_username(username.data) is not None:
            raise ValidationError('That username already exist. Please choose another one')

    def validate_email(self, email):
        if User.find_by_email(email.data) is not None:
            raise ValidationError('That email already exist. Please choose another one')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            if User.find_by_username(username.data) is not None:
                raise ValidationError('That username already exist. Please choose another one')

    def validate_email(self, email):
        if email.data != current_user.email:
            if User.find_by_email(email.data) is not None:
                raise ValidationError('That email already exist. Please choose another one')

class MonitorringForm(FlaskForm):
    paym_available = SelectMultipleField('PAYM users')
    select_paym_user = SubmitField('SELECT')
    remove_paym_user = SubmitField('REMOVE')
    test_data_selected = SelectMultipleField('Selected users', choices=[])
    select_payg_user = SubmitField('SELECT')
    remove_payg_user = SubmitField('REMOVE')
    payg_available = SelectMultipleField('PAYG users')
    paym_requests_available = SelectMultipleField('PAYM requests', choices=[])
    select_paym_request = SubmitField('SELECT')
    remove_paym_request = SubmitField('REMOVE')
    requests_selected = SelectMultipleField(choices=[(1, 'self'), (2, 'billing-accounts'), (3, 'mobile-subscriptions')])
    select_payg_request = SubmitField('SELECT')
    remove_payg_request = SubmitField('REMOVE')
    payg_requests_available = SelectMultipleField('PAYG requests', choices=[])
    result_area = TextAreaField(label='Results will be here')
    start_monitoring = SubmitField(label="START MONITORING")