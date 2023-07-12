from flask import Flask, render_template, request
import os
import pickle
import pandas as pd
import sqlite3

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html')
