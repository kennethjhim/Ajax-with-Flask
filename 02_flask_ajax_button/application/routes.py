from application import app
from flask import render_template, session, request, jsonify

@app.route("/index")
@app.route("/")
def index():

    if not session:
        session['favorites'] = []
        session['unfavorites'] = []
        session.modified = True

    return render_template("index.html", favorites=session['favorites'], unfavorites=session['unfavorites'])


@app.route("/favorite", methods = ['GET', 'POST'])
def favorite():
    print(session)

    if request.method == 'POST':
        id = request.form.get('id')[-3:]
        print(id)

    if id not in session['favorites']:
        session['favorites'].append(id)

        if id in session['unfavorites']:
            session['unfavorites'].remove(id)

        session.modified = True
    print(session)
    return "True"


@app.route("/unfavorite", methods = ['GET', 'POST'])
def unfavorite():
    print(session)

    if request.method == 'POST':
        id = request.form.get('id')[-3:]
    
    if id not in session['unfavorites']:
        session['unfavorites'].append(id)

        if id in session['favorites']:
            session['favorites'].remove(id)

        session.modified = True

    print(session)
    return "True"