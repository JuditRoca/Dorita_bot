from datetime import datetime
from flask import Flask, render_template, request
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
import os
import pandas as pd
import sqlite3

os.chdir(os.path.dirname(__file__))
api_key = os.environ.get["api_key"] 
serpapi_key = os.environ.get["serpapi"] 

app = Flask(__name__)
app.config['DEBUG'] = True

historial = []
bbdd = 'data/bbdd.bd'

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Basic function where the user asks something and returns the answer from ChatGPT. It will also save it in the Cloud DDBB, in this case, AWS.

    Parameters 
    ----------
    Type in the interface what you want to ask and it will return the answer.
    """
    try:
        
        if request.method == 'GET':
            return render_template('index.html')
        
        if request.form['question']:
            question = request.form['question']
            historial.append(question)
        
            # Load the model
            llm = OpenAI()

            # Load in some tools to use
            tools = load_tools(["serpapi", "llm-math"], llm=llm)

            # Finally, let's initialize an agent with:
            # 1. The tools
            # 2. The language model
            # 3. The type of agent we want to use.

            agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)


            # Now let's test it out!
            respuesta = agent.run(question)
            now = datetime.now()

            historial.append(respuesta, now)
            
            return render_template('index2.html', text_output = respuesta)

    except:

        return render_template('index3.html')
    
app.run(host="0.0.0.0", port=5000, debug=True)