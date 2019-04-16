import sqlite3

f1 = open("books.csv", "r")
list1 = []
for rec in f1:
    list1.append(rec.rstrip().split(','))

f1.close()
print list1

conn = sqlite3.connect("books.db")
cursor =conn.cursor()

#cursor.execute("""CREATE TABLE books
 #               (id int, title text,author text)
  #               """)

cursor.executemany("INSERT INTO books VALUES (?,?,?)", list1)
conn.commit()

print "Printing from db"
for id,book,author in cursor.execute("SELECT * FROM books"):
    print id, book, author

cursor.execute("DELETE FROM books")
conn.commit()
conn.close()
