from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
	print "in the / route"
	return 'Hello World'

@app.route('/bar')
def bar():
	name = request.args.get('name')
	print name
	return "Your name is " + name

if __name__ == '__main__':
    app.run()