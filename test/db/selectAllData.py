import sqlite3

conn = sqlite3.connect('../../db/sensorData.db')
c = conn.cursor()

cursor = c.execute("SELECT * from fieldsensor")

for row in cursor:
    print(row)

conn.close()

