from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, jsonify
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
import os
import pymysql
from dotenv import load_dotenv
load_dotenv()


os.chdir(os.path.dirname(__file__))
api_key = os.environ.get("OPENAI_API_KEY")
serpapi_key = os.environ.get("SERPAPI_API_KEY")
username = os.environ.get("user_bd")
password = os.environ.get("pass_bd")
host = os.environ.get("host")
db = pymysql.connect(host = host,
                        user = username,
                        password = password,
                        cursorclass = pymysql.cursors.DictCursor)

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
            cursor = db.cursor()
            sql = "INSERT INTO chatbot_records (pregunta, respuesta, timestamp) VALUES (%s, %s)"
            cursor.execute(sql, (question, respuesta, now))
            db.commit()
            db.close()
            historial.append({"message": respuesta, "from_user": False, "timestamp": now})

            return render_template('index.html', historial=historial)
    except:
        return render_template('index.html', historial=historial)
    
@app.route('/get_history', methods=['GET'])
def get_all():
    cursor = db.cursor()

    sql = '''SELECT * FROM chatbot_records'''
    cursor.execute(sql)
    history = cursor.fetchall()
    db.close()
    return jsonify(history)

app.run(host="0.0.0.0", port=5000, debug=True)