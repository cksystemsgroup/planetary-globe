import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="database"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM globe")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
