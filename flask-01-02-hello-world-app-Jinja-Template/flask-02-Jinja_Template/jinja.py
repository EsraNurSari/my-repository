#Import Flask and render_template modules
from flask import Flask, render_template

#Create an object named `app` from imported Flask module
app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1=34, number2=45)

@app.route("/function")
def function():
    variable1 = 12
    variable2 = 4
    return render_template("body.html", num1 = variable1, num2 = variable2, multp=variable1*variable2)

if __name__ == "__main__":
    app.run(debug=True)