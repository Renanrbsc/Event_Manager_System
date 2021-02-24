import mysql.connector as db

mysql_db = db.connect(host="localhost",
                      user="user",
                      passwd="12345",
                      db="managerevent_db")

print(mysql_db.database)
