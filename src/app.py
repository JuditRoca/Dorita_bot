from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
import os
import pandas as pd
import sqlite3
from dotenv import load_dotenv
load_dotenv()


os.chdir(os.path.dirname(__file__))
api_key = os.environ.get("OPENAI_API_KEY")
serpapi_key = os.environ.get("SERPAPI_API_KEY")

 # Load the model
llm = OpenAI(api_key=api_key)
tools = load_tools(["serpapi"], serpapi_key=serpapi_key)


app = Flask(__name__)
app.config['DEBUG'] = True

historial = []

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
            historial.append({"message": question, "from_user": True})  # Agregar la pregunta al historial como una entrada del usuario

            agent = initialize_agent(tools, llm, agent="zero-shot-react-description", language="es", verbose=True)
            respuesta = agent.run(question)

            now = datetime.now()
            historial.append({"message": respuesta, "from_user": False, "timestamp": now})

            return render_template('index.html', historial=historial)
    except:
        return render_template('index.html', historial=historial)
    

app.run(host="0.0.0.0", port=5000, debug=True)