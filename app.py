from flask import Flask
from flask import request
import Tkinter
import tkMessageBox

app = Flask(__name__)

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

@app.route('/')
def hello_world():
	print "in the / route"
	return 'Hello World'
	B = Tkinter.Button(top, text ="Hello", command = helloCallBack)


@app.route('/bar')
def bar():
	name = request.args.get('name')
	address = request.args.get('address')
	print name
	return "Your name is " + name + " and your address is " + address




if __name__ == '__main__':
    app.run()