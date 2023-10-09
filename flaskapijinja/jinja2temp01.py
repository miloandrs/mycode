#!/usr/bin/env python3
"""
Jinja test with flask
"""
# imports
from flask import Flask
from flask import render_template


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("hellobasic.html")


def main():
    """runtime code"""
    app.run(host="0.0.0.0", port=2224)

if  __name__ == '__main__':
    main()
