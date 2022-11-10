from crate import client
import time

connection = client.connect("http://localhost:4200/", username="crate")

cursor = connection.cursor()

#cursor.execute("""CREATE TABLE people ( name text, date text, country text, age integer)""")

cursor.execute("""INSERT INTO people (name, date, country, age)
            VALUES (?, ?, ?, ?)""",("Joel Bra", "09/07/2001", "España", 21))

cursor.execute("DELETE FROM people WHERE country = ?", ('España',))
time.sleep(5)
#cursor.execute("UPDATE people set country = 'Españita' WHERE NAME = 'Joel Bra'")
cursor.execute("SELECT * FROM people WHERE name = 'Joel Bra'")
res = cursor.fetchone()
print(res)
