from datetime import datetime
from flask import Flask, render_template, request, jsonify
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

 # Load the model
llm = OpenAI()
tools = load_tools(["serpapi"], serpapi_key=serpapi_key)


app = Flask(__name__)
app.config['DEBUG'] = True

historial = []

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Función básica del home que sirve para preguntar y solicitar información al chatbot, conectándose a Langchain y OpenAI
    También almacena un registro de todas las solicitudes y sus respuestas junto a la hora de ejecución en una base de datos externa.

    Returns: 
        Respuesta en la misma interfaz de la aplicación.
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

            db = pymysql.connect(host = host,
                                 user = username,
                                 password = password,
                                 db= 'gptgoogler_database',
                                 cursorclass = pymysql.cursors.DictCursor)
            cursor = db.cursor()
            sql = "INSERT INTO chatbot_records (pregunta, respuesta, timestamp) VALUES (%s, %s, %s)"
            cursor.execute(sql, (question, respuesta, now))
            db.commit()
            db.close()

            return render_template('index.html', historial=historial)
    except:
        return render_template('index.html', historial=historial)
    
@app.route('/get_history', methods=['GET'])
def get_all():
    """
    Función para obtener todos los registros de la base de datos externa.

    Returns:
        Todos los registros existentes en la base de datos, ordenados por orden de consulta.
        
    """
    db = pymysql.connect(host = host,
                        user = username,
                        password = password,
                        db= 'gptgoogler_database',
                        cursorclass = pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = '''SELECT * FROM chatbot_records'''
    cursor.execute(sql)
    history = cursor.fetchall()
    db.close()
    return jsonify(history)

app.run(host="0.0.0.0", port=5000, debug=True)