from sqlalchemy.dialects.postgresql import JSON

# custom imports
from src.app import db


class Question(db.Model):
    """
    Table for storing Questions.
    """
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if not key == "id":
                setattr(self, key, value)


class Choice(db.Model):
    """
    Table for storing Choices.
    """
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    text = db.Column(db.String())

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if not key == "id":
                setattr(self, key, value)


class Selection(db.Model):
    """
    Table for storing Selections.
    """
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    choice_id = db.Column(db.Integer, db.ForeignKey('choice.id'))

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if not key == "id":
                setattr(self, key, value)
