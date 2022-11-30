from crate import client
from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/retrievedata',methods=['GET'])
def retrieve_data():
    connection = client.connect("http://10.5.0.4:4200/", username="crate")
    if connection:
        cursor = connection.cursor()
        cursor.execute("select table_name from information_schema.tables WHERE table_name = 'tasks' limit 100")
        exists = cursor.fetchone()
        if (not exists):
            cursor.execute("""CREATE TABLE tasks (name text, task text, date text)""")
            cursor.execute("COPY tasks FROM 'file:///db-data/tasks_1_.json'")
            cursor.execute("COPY tasks FROM 'file:///db-data/tasks_2_.json'")
            time.sleep(1)
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        connection.close()
    retorno = {"lTareas": []}
    for t in tasks:
        retorno["lTareas"].append({"name": t[0], "task": t[1], "date": t[2]})
    
    return jsonify(retorno)

@app.route('/newentry', methods=['POST'])
def new_entry():
    name = request.form['name']
    task = request.form['task']
    date = request.form['date']

    connection = client.connect("http://10.5.0.4:4200/", username="crate")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO "doc"."tasks" (name, task, date) 
                   VALUES (?, ?, ?)""",(name, task, date))
    connection.close()

    return "Succesfull"

app.run(host='0.0.0.0', port=4201)
