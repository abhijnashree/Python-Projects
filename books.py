import sqlite3

con=sqlite3.connect("books_db.sqlite3")
cur=con.cursor()

try:
	cur.execute("create table books_available(id integer primary key,name text,rating integer)")
except sqlite3.OperationalError:
	print("table already exists...!!!")	

cur.execute("""insert into books_available values(77,"LORD OF THE RINGS",4)""")
cur.execute("""insert into books_available values(88,"THE RECKONING",3)""")
cur.execute("""insert into books_available values(99,"THE SECRET",5)""")


con.commit()