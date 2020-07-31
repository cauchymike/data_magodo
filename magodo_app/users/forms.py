from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed
from magodo_app.models import User
from flask_login import current_user


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('UserName',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match!')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    full_name = StringField('Full Name', validators=[DataRequired(), Length(max=70)])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    house_type = SelectField('Type of House',
                             choices=[('bun', 'Bungalow'),
                                      ('two', 'More than One Storey'),
                                      ('ds', 'Duplex'), ('unc', 'Uncompleted Building')],
                             validators=[DataRequired()])
    house_number = StringField('House Number', validators=[DataRequired()])
    street_name = StringField('Name of Street', validators=[DataRequired()])
    house_describe = TextAreaField('Further Description',
                                   validators=[DataRequired(), Length(min=10, message = 'Description too short')])

    submit = SubmitField('Register!')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been registered already!')


class UpdateUserForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('UserName',validators=[DataRequired()])
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been registered already!')

