import mysql.connector
db = mysql.connector.connect(user = 'root',password='root', host='localhost',database='TEST1')
code ="DROP DATABASE `test` ;"

mycursor = db.cursor()
mycursor.execute("")
