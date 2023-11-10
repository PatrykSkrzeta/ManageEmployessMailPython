from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '589327859023JF84JF8RFJ4F3008FeE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
db = SQLAlchemy(app)

from application import routes
