from datetime import datetime
import pandas as pd
import pymysql
from sqlalchemy import create_engine

username = ""
password = ""
host = ''
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