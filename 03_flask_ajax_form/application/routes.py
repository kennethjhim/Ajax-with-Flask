from application import app
from flask import session, render_template, request, jsonify

@app.route("/index")
@app.route("/")
def index():

    return render_template('index.html')


@app.route("/process_measurements", methods = ['GET', 'POST'])
def process_measurements():
	if request.method == 'POST':
		try:
			length = float(request.form.get('length')) or 'length'
			width = float(request.form.get('width')) or 'width'
			height = float(request.form.get('height')) or 'height'

			volume = length * width * height
		except:

			res = '''
				<p>There were errors on: length, width, height</p>
				<p><a href="/">Back</a></p>
			'''

		res = '''
			<p>The total volume is: {} </p>
			<p><a href="/">Back</a></p>
		'''.format(volume)

	return res
