from datetime import datetime
from flask import Flask, render_template, request
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
import os
import pandas as pd
import sqlite3

os.chdir(os.path.dirname(__file__))
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "5067b007321f10e48e326d4eb4541a31e265c60d4975babe7f032261dd340dfd"

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

            historial.append(respuesta)
            
            return render_template('index.html', historial = historial)

    except:
        return render_template('index.html')
    
app.run(host="0.0.0.0", port=5000, debug=True)