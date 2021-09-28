import mysql.connector
import json
from flask import Flask
from werkzeug.utils import import_string
# from settings import DevelopmentConfig

app = Flask(__name__)
# app.config.from_object(DevelopmentConfig())
DB_SERVER = import_string('settings.DevelopmentConfig')()
DB_USER = import_string('settings.DevelopmentConfig')()
DB_PASSWORD = import_string('settings.DevelopmentConfig')()
DB_URI = import_string('settings.DevelopmentConfig')()

@app.route('/')
def hello_world():
  return 'Hello, Docker!'

@app.route('/widgets')
def get_widgets() :
  mydb = mysql.connector.connect(
    host=DB_SERVER,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_URI
  )
  cursor = mydb.cursor()


  cursor.execute("SELECT * FROM widgets")

  row_headers=[x[0] for x in cursor.description] #this will extract row headers

  results = cursor.fetchall()
  json_data=[]
  for result in results:
    json_data.append(dict(zip(row_headers,result)))

  cursor.close()

  return json.dumps(json_data)

@app.route('/initdb')
def db_init():
  mydb = mysql.connector.connect(
    host=DB_SERVER,
    user=DB_USER,
    password=DB_PASSWORD
  )
  cursor = mydb.cursor()

  cursor.execute("DROP DATABASE IF EXISTS inventory")
  cursor.execute("CREATE DATABASE inventory")
  cursor.close()

  mydb = mysql.connector.connect(
    host=DB_SERVER,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_URI
  )
  cursor = mydb.cursor()

  cursor.execute("DROP TABLE IF EXISTS widgets")
  cursor.execute("CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))")
  cursor.close()

  return 'init database'

if __name__ == "__main__":
  app.run(host ='0.0.0.0')
