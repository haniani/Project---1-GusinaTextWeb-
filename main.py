# -*- coding: utf-8 -*-

import flask
from flask import render_template
from flask import Flask

try:
    from os import getuid

except ImportError:
    def getuid():
        return 4000

app = Flask(__name__)

app.config['ASSETS_DEBUG'] = True
app.debug = True

@app.route("/")

def index():
    return flask.render_template('hello.html')

@app.route("/plans")

def plans():
    return flask.render_template('plans.html')

if __name__ == "__main__":
    app.run(port=getuid() + 1000)
