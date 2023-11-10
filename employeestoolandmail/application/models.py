from application import db
from datetime import datetime, date

class employee(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    birth_day = db.Column(db.Date, nullable=False, default=date.today)
    adres = db.Column(db.String)
    phone_number = db.Column(db.String)
    salary = db.Column(db.Integer)
    position = db.Column(db.String)
    email = db.Column(db.String(200), unique=True, nullable=False)
