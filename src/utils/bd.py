import pymysql
import os

username = os.environ.get["user_bd"]
password = os.environ.get["pass_bd"]
host = os.environ.get["host"]
port = 3306

db = pymysql.connect(host = host,
                     user = username,
                     password = password,
                     cursorclass = pymysql.cursors.DictCursor)

cursor = db.cursor()

create_db = '''CREATE DATABASE gptgoogler_database'''
cursor.execute(create_db)

cursor.connection.commit()
use_db = ''' USE gptgoogler_database'''
cursor.execute(use_db)

create_table = '''
CREATE TABLE chatbot_records (
    id INT NOT NULL AUTO_INCREMENT,
    pregunta TEXT,
    respuesta TEXT,
    timestamp TIMESTAMP,
    PRIMARY KEY (id)
)
'''
cursor.execute(create_table)

db.commit()

db.close()