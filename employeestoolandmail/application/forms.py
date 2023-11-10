from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, DateField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

class EmployeeForm(FlaskForm):
    first_name = StringField('Name', validators=[DataRequired()])
    last_name = StringField('Surrname', validators=[DataRequired()])
    birth_day = DateField("Birth Day", validators=[DataRequired()])
    adres = StringField('Adres', validators=[DataRequired()])
    phone_number = StringField('Phone', validators=[DataRequired()])
    salary = StringField('Salary', validators=[DataRequired()])
    position = SelectField('Position', choices=[('back-end developer', 'Back-end Developer'), ('front-end developer', 'Front-end Developer'), ('data analyst', 'Data Analyst')], validators=[DataRequired()])
    email = StringField('Mail')
    enter = SubmitField('Add Employee')


class SearchForm(FlaskForm):
    search = StringField('')
    submit = SubmitField('Submit')
    undo = BooleanField('Undo')

class EmailForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    send = SubmitField('Send')