from sqlalchemy.dialects.postgresql import JSON

# custom imports
from src.app import db


class Question(db.Model):
    """
    Table for storing Questions.
    """
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())


class Choice(db.Model):
    """
    Table for storing Choices.
    """
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    text = db.Column(db.String())

