#Import Flask and render_template modules
from flask import Flask, render_template

#Create an object named `app` from imported Flask module
app = Flask(__name__)

#Create a function named `head` which sends number `number1` and `number2` variables to the `index.html`. 
#Use these variables into the `index.html` file. Assign a URL route the `head` function with decorator `@app.route('/')`
@app.route("/")
def head():
    return render_template("index.html", number1=34, number2=45)

#Create a function named `number` which sends number `num1` and `num2` and sum of them to the `index.html`. Use these variables into the `body.html` file. 
#Assign a URL route the `number` function with decorator `@app.route('/sum')`
@app.route("/function")
def function():
    variable1 = 12
    variable2 = 4
    return render_template("body.html", num1 = variable1, num2 = variable2, multp=variable1*variable2)

if __name__ == "__main__":
    app.run(debug=True)