from flask import Flask, render_template, request
import os
import pickle
import pandas as pd
import sqlite3
import openai

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    try:
        api_key = request.form['api_key']
        openai.api_key = api_key
        #openai.api_key = open(api_key_path, "r").read()
        variable = request.form['variable']
        response = openai.Completion.create(engine = "text-davinci-003",
                                        prompt = variable + "Respuesta corta, por favor",
                                        max_tokens=1000, temperature=0.8)
        

    
    except:
        return render_template('index_3.html')
    
    
    app.run(host="0.0.0.0", port=5000, debug=True)