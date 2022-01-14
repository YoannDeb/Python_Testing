from wtforms import Form, StringField, validators


class RegistrationForm(Form):
    email = StringField('Email:', [validators.InputRequired(), validators.Length(max=100), validators.Email()])
