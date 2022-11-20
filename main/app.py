from crate import client
import time

connection = client.connect("http://localhost:4200/", username="crate")

cursor = connection.cursor()
cursor.execute("select table_name from information_schema.tables WHERE table_name = 'people' limit 100")
exists = cursor.fetchone()
if (not exists):
    cursor.execute("""CREATE TABLE people ( name text, date text, country text)""")

while True:
    print("1. Introducir datos\n2. Borrar datos\n3. Ver datos\n4. Salir")
    option = input("Elige una opción: ")
    if option == "1":
        name = input("Escribe tu nombre: ")
        date = input ("Escribe tu fecha de nacimiento: ")
        country = input("Escribe tu país: ")
        cursor.execute("""INSERT INTO people (name, date, country)
            VALUES (?, ?, ?)""",(name, date, country))
        print("Se ha añadido la entrada correctamente\n")
    elif option == "2":
        name = input("Escribe el nombre de la entrada que quieres borrar: ")
        cursor.execute("DELETE FROM people WHERE name = ?", (name,))
        print("Se ha borrado la entrada correctamente\n")
    elif option == "3":
        name = input("Escribe el nombre de la entrada que quieres consultar: ")
        cursor.execute("SELECT * FROM people WHERE name = ?", (name,))
        res = cursor.fetchone()
        print(str(res) + "\n")
    elif option == "4":
        exit(0)