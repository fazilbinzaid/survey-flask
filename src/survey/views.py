from flask import jsonify

# custom imports
from src.app import app
from .models import *


@app.route("/api/questions/")
def list_questions():
    """
    View for listing all the questions.
    """
    questions = Question.query.all()
    return jsonify(questions)
