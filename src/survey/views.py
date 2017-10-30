import os
from flask import jsonify, render_template, request, redirect, url_for, send_from_directory
from flask.views import MethodView

# custom imports
from src.app import app, db
from src.auth.decorators import requires_auth, check_auth
from .models import *


@app.route("/api/questions/")
def list_questions():
    """
    View for listing all the questions.
    """
    questions = Question.query.all()
    return jsonify(questions)


@app.route('/css/<string:filename>/')
def send_css(filename):
    return send_from_directory('assets/css', filename)

@app.route('/js/<string:filename>/')
def send_js(filename):
    return send_from_directory('assets/js', filename)

@app.route('/bundle/<string:filename>/')
def send_bundle(filename):
    return send_from_directory('assets/dist', filename)

@app.route('/node_modules/<path:filename>/')
def send_node_modules(filename):
    return send_from_directory('assets/node_modules', filename)


@app.route("/api/login/", methods=['GET', 'POST'])
def login():
    context = {}
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if check_auth(username, password):
            return redirect(url_for('questions_list'))
        context = { 'message': 'Invalid Credentials' }
    return render_template("login.html", **context)

@app.route("/api/admin/questions/", methods=['GET'])
def questions_list():
    questions = Question.query.all()
    return render_template("questions_list.html", questions=questions)


@app.route("/api/admin/create_question/", methods=['POST'])
def create_question():
    question_text = request.json.get('question_text')
    choices = request.json.get('choice_list')
    question = Question(text=question_text)
    db.session.add(question)
    db.session.commit()
    for choice_text in choice_list:
        db.session.add(Choice(question_id=question.id, text=choice_text))
    db.session.commit()
    return jsonify({"success": True, "message": "Database updated."})




