import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="abdb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE nonprotein_complex (name VARCHAR(35))")

sql4 = "INSERT INTO nonprotein_complex (name) VALUES (%s)"
val4 = [
  ('1A4K',),
  ('1A6V',),
  ('1AJ7',),
  ('1AXS',),
  ('1BAF',),
  ('1CIE',),
  ('1C5C',),
  ('3UJT',),
  ('3WHX',),
  ('3ZL4',),
  ('4AMK',),
  ('4FAB',),
  ('4FNL',),
  ('6CBJ',),
  ('6DB8',),
  ('6DW2',)
]
mycursor.executemany(sql4, val4)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


