#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/") #This is called a decorator or endpoint for flask
def hello_world():
   return "Hello World"

@app.route("/hello")
def test():
    return "OMG I can't believe this works"

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}"



if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE

