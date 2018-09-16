import sqlite3

conn = sqlite3.connect('../../db/sensorData.db')
c = conn.cursor()
data = (1532743225,'4DB0D9',-126,'6CE1',6.00,28.78,16.53,43,'payload')

print(data)


c.execute("INSERT INTO  fieldsensor (ts,deviceID,rssi,station,snr,lat,lng,seqNumber,data) VALUES (?,?,?,?,?,?,?,?,?)",data)

conn.commit()
conn.close()



