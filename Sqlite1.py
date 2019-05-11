import sqlite3

conn = sqlite3.connect('amirdb.db')
c = conn.cursor()
#c.execute("CREATE TABLE phone_book (name text, phone text)")
#c.execute("INSERT INTO phone_book VALUES ('Mehdi','555')")
#conn.commit()
c.execute("SELECT name,phone FROM phone_book")
print(c.fetchall())
conn.close()