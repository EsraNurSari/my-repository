#Import Flask module
from flask import Flask

#Create an object named `app` from imported Flask module
app = Flask(__name__)

#Create a function `hello` which returns a string `Hello World`
#Assign a URL route the `hello` function with decorator `@app.route('/')`
@app.route("/")
def head():
    return "<h1>You are gonna be a good DevOps and AWS Solution Architech</h1>"

#Create a function `second` which returns a string `This is the second page`
#Assign a URL route the `second` function with decorator `@app.route('/second')`
@app.route("/second")
def second():
    return "This is the second page"

#Create a function `third` which returns a string `This is the subpage of third page`
#Assign a URL route the `third` function with decorator `@app.route('/third/subthird')`
@app.route("/third/subthird")
def third():
    return "This is the subpage of third page"

#Create a dynamic url which takes id number dynamically and return with a massage which show id of page
@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'

if __name__ == '__main__':
    app.run(debug=True)

#if __name__=="__main__":
    #app.run(debug=True)

