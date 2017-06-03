from flask import Flask, json
app = Flask(__name__)

@app.route('/Interview')
def json_info():
	info = {"Name" : "Daryan Hanshew", "Phone Number": 2535145920, "Email": "dhanshew@uw.edu"}
	return json.dumps(info)

@app.route('/')
def index():
	return 'Type /Interview for JSON object'

if __name__ == '__main__':
    app.run(debug=True)