import os
from flask import jsonify, render_template, request, redirect, url_for, send_from_directory
from flask.views import MethodView

# custom imports
from src.app import app, db
from src.auth.decorators import requires_auth, check_auth
from .models import *


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
    response_array = []
    for question in questions:
        choice_array = []
        for choice in Choice.query.filter_by(question_id=question.id):
            choice_array.append({
                    'id': choice.id,
                    'text': choice.text,
                    'count': Selection.query.filter_by(question_id=question.id, choice_id=choice.id).count()
                })
        response_array.append({
                'id': question.id,
                'text': question.text,
                'choices': choice_array
            })
    return render_template("questions_list.html", questions=reversed(response_array))


@app.route("/api/admin/create_question/", methods=['POST'])
def create_question():
    question_text = request.json.get('question_text')
    choices = request.json.get('choice_list')
    question = Question(text=question_text)
    db.session.add(question)
    db.session.commit()
    for choice_text in choices:
        db.session.add(Choice(question_id=question.id, text=choice_text))
    db.session.commit()
    return jsonify({"success": True, "message": "Database updated."})


@app.route("/api/admin/edit_choices/", methods=['POST'])
def edit_choices():
    choice_list = request.json.items()
    for choice_id, value in choice_list:
        choice = Choice.query.get(int(choice_id))
        choice.text = value
    db.session.commit()
    return jsonify({"success": True, "message": "Database updated."})


@app.route("/api/survey/", methods=['POST'])
def survey():
    return jsonify({})

@app.route("/api/questions/", methods=['GET'])
def list_all_questions():
    questions = Question.query.all()
    response = []
    for question in questions:
        response.append({
            'question': {
                'id': question.id,
                'text': question.text
            },
            'choices': [{
                'id': choice.id,
                'text': choice.text
            } for choice in Choice.query.filter_by(question_id=question.id)]
        })
    return jsonify({ 'data': response })

@app.route("/api/make_selections/", methods=['GET', 'POST'])
def make_selections():
    if not request.method == "POST":
        return render_template("sticky.html")
    data = request.json
    for selection in data:
        new_selection = Selection(question_id=int(selection['question']), choice_id=int(selection['choice']))
        db.session.add(new_selection)
    db.session.commit()
    return jsonify({"success": True, "message": "Database updated."})

@app.route("/api/code/", methods=['GET'])
def code_view():
    return jsonify('''document.write('<style>#chat_box{position: fixed;bottom: 0px;right: 40px;width: 350px;border-right: 1px solid #ccc;border-left: 1px solid #ccc;border-radius: 5px 5px 0 0;box-sizing: border-box;z-index: 9999;}#chat_box_head , #chat_box_body{width: 350px;cursor: pointer;}#chat_box_head{background-color: #c00;color: white;padding: 10px;border-radius: 5px 5px 0 0;}#chat_box_body{height: 0;}.height{height: 300px!important;}iframe{height:290px;border: 0;}.chat_div_class{height: 300px;overflow-y: scroll;overflow-x: hidden;}</style><div id="chat_box" onclick="toggle()"><div id="chat_box_head">Survey</div><div id="chat_box_body"><iframe src="http://localhost:5000/api/make_selections/" width="98%" ></iframe></div></div><script>function toggle(){var element=document.getElementById("chat_box");element.classList.toggle("chat_div_class");}<\/script>');'''
        )

# @app.route("/api/admin/reports/", methods=['GET'])
# def show_reports():






