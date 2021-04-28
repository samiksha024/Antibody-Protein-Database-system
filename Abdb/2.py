import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="abdb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE free_chains (name VARCHAR(255))")

sql = "INSERT INTO free_chains (name) VALUES (%s)"
val = [
  ('1MAK',),
  ('1A8J',),
  ('1MCB',),
  ('1MCE',),
  ('1MCF',),
  ('1MCH',),
  ('1MCJ',),
  ('1MCK',)
]

sql = "INSERT INTO free_chains (name) VALUES (%s)"
val = [
  ('1MAK',),
  ('1A8J',),
  ('1MCB',),
  ('1MCE',),
  ('1MCF',),
  ('1MCH',),
  ('1MCJ',),
  ('1MCK',)
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


