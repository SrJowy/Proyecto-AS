from crate import client
from flask import Flask, request, jsonify
from flask_cors import CORS

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


#connection = client.connect("http://localhost:4200/", username="crate")
#
#cursor = connection.cursor()
#cursor.execute("select table_name from information_schema.tables WHERE table_name = 'people' limit 100")
#exists = cursor.fetchone()
#if (not exists):
#    cursor.execute("""CREATE TABLE people ( name text, date text, country text)""")
#
#while True:
#    print("1. Introducir datos\n2. Borrar datos\n3. Ver datos\n4. Salir")
#    option = input("Elige una opción: ")
#    if option == "1":
#        name = input("Escribe tu nombre: ")
#        date = input ("Escribe tu fecha de nacimiento: ")
#        country = input("Escribe tu país: ")
#        cursor.execute("""INSERT INTO people (name, date, country)
#            VALUES (?, ?, ?)""",(name, date, country))
#        print("Se ha añadido la entrada correctamente\n")
#    elif option == "2":
#        name = input("Escribe el nombre de la entrada que quieres borrar: ")
#        cursor.execute("DELETE FROM people WHERE name = ?", (name,))
#        print("Se ha borrado la entrada correctamente\n")
#    elif option == "3":
#        name = input("Escribe el nombre de la entrada que quieres consultar: ")
#        cursor.execute("SELECT * FROM people WHERE name = ?", (name,))
#        res = cursor.fetchone()
#        print(str(res) + "\n")
#    elif option == "4":
#        exit(0)