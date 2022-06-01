from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User
# python classes will be converted to html forms

class RegistrationForm(FlaskForm):
    username = StringField("Username", 
                            validators=[DataRequired(), Length(min=2, max=20)]) # username in html
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", 
                                    validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    #checking if the user and email are already in use
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        #querying the database. if a user is returned, field input is already taken
        if user:
            raise ValidationError("That username is taken. Please choose a different one.")

    def validate_email(self, email):
        user = User.query.filter_by(username=email.data).first()
        if user:
            raise ValidationError("That user is taken. Please choose a different one or login.")


class LoginForm(FlaskForm):
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")

    submit = SubmitField("Login")

