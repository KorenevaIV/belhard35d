import sqlite3

conn = sqlite3.connect('../12/db.sqlite3')
cur = conn.cursor()
cur.execute('''
   UPDATE categories 
   SET name = ?
   WHERE id = 1;
''', ('Food', ))
conn.commit()

cur.execute('''
    ALTER TABLE users ADD surname VARCHAR(32);
''')
conn.commit()
