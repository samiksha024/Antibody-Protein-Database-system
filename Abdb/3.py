import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="abdb"
)

mycursor = mydb.cursor()


sql3 = "INSERT INTO protein_complex (code_name) VALUES (%s)"
val3 = [
  ('3H3P',),
  ('3HAE',),
  ('3HB3',),
  ('3HI',),
  ('3HI6',),
  ('4OKV',),
  ('4OLV',),
  ('4OLW',),
  ('4OLX',),
  ('4OLZ',),
  ('4OMO',),
  ('5K9K',),
  ('5K9O',),
  ('5K9Q',),
  ('5KEL',),
  ('5KEM',),
  ('5KEN',),
  ('5KOV',)
]
mycursor.executemany(sql3, val3)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


