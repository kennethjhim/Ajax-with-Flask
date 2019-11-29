import os
from application import app
from flask import session, render_template, request, jsonify

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search")
def search():
    query = request.form.get('q')

    return render_template(search.html, query=query)

@app.route("/autosuggest/q=<q>")
def autosuggest(q):

    query = q.lower() or ''

    # print(os.getcwd())
    with open('application/us_passenger_trains.txt', 'r') as f:
      choices = [l.strip() for l in f.readlines()]

    print(choices)
    suggestions = [s for s in choices if s.lower().startswith(query)]
    # print(suggestions)
    suggestions.sort()

    max = 5
    top_suggestions = suggestions[0:max]

    return jsonify(top_suggestions)