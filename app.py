from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
	return '''<!DOCTYPE html>

<html>
<head>
    <title>College Meal Plans</title>
</head>
<body>
    <h1><font color="red">College Students, </font></h1>
    <p><font color="blue">No time to cook? No recipes off the top of your head?</font></p>
    <h2><font color="green">No Problem!</font></h2>
    <p><font color="blue">With this website, you will no longer need to waste time trying to find the right recipe.<br>
        Just enter how long you have to cook and what ingredients you have and we'll do the rest<br>
        (except make the food!).</font></p>
    <form name="TimeToCook">
        Time to cook (in minutes): <br>
        <input type="number" name="timetocook"><br>
    </form>
    <form name="Vegetables">
        <br>Vegetables: <br>
        <input type="checkbox" name="Onions">Onions<br>
        <input type="checkbox" name="Bell Peppers">Bell Peppers<br>
        <input type="checkbox" name="Tomatoes">Tomatoes<br>
        <input type="checkbox" name="Carrots">Carrots<br>
        <input type="checkbox" name="Potatoes">Potatoes<br>
        <input type="checkbox" name="Jalapenos">Jalapenos<br>
    </form>
    <form name="Fruits">
        <br>Fruits: <br>
        <input type="checkbox" name="Apples">Apples<br>
        <input type="checkbox" name="Bananas">Bananas<br>
        <input type="checkbox" name="Oranges">Oranges<br>
        <input type="checkbox" name="Pineapple">Pineapple<br>
        <input type="checkbox" name="Watermelon">Watermelon<br>
    </form>
    <form name="Meat/Poultry">
        <br>Meat/Poultry: <br>
        <input type="checkbox" name="Chicken">Chicken<br>
        <input type="checkbox" name="Beef">Beef<br>
        <input type="checkbox" name="Fish">Fish<br>
        <input type="checkbox" name="Eggs">Eggs<br>
        <input type="checkbox" name="Pork">Pork<br>
    </form>
    <form name="Grains">
        <br>Grains: <br>
        <input type="checkbox" name="Rice">Rice<br>
        <input type="checkbox" name="Sliced Bread">Sliced Bread<br>
        <input type="checkbox" name="Tortillas">Tortillas<br>
        <input type="checkbox" name="Pasta">Pasta<br>
    </form>
    <form name="Miscellaneous">
        <br>Miscellaneous: <br>
        <input type="checkbox" name="Oil">Oil<br>
        <input type="checkbox" name="Garlic">Garlic<br>
        <input type="checkbox" name="Salt">Salt<br>
        <input type="checkbox" name="Milk">Milk<br>
    </form>
    <form>
        <br><button id="findrecipe" onclick="myFunction()">Find your recipe!</button>
    </form>
    <!--<p id="printTime"></p>
    <script>
        function myFunction() {
            var time = document.forms["TimeToCook"]["timetocook"].value;
            document.getElementById("printTime").innerHTML = "You have " + time + " to cook."
        }
    </script>-->

</body>
</html>'''

@app.route('/bar')
def bar():
	name = request.args.get('name')
	address = request.args.get('address')
	print name
	return "Your name is " + name + " and your address is " + address

@app.route('/<name>')
def hello_name(name):	
	return "Hello " + name


if __name__ == '__main__':
    app.run()