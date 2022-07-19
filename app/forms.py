from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, InputRequired, length

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")