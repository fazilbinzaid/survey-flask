import os

from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# custom imports
from settings import CONFIG


app = Flask(__name__)
app.config.from_object(CONFIG)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from src.survey import *


@app.route('/')
def hello():
    return redirect(url_for('login'))
