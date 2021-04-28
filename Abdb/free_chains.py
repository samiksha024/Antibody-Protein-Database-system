import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="abdb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO free_chains (name) VALUES (%s)"
val = ("1MAJ",)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
