import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(24) NOT NULL,
    email VARCHAR(24) UNIQUE
    );
''')
conn.commit()
# cur.executemany('''
# INSERT INTO users(name, email)
# VALUES(?, ?);
# ''', (('Vasya', 'vasya@gmail.com'), ('Toma', 'toma@gmail.com'), ('Irina', 'Irina@gmail.com')))
# conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS statuses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(10) UNIQUE
    );
''')
conn.commit()
# cur.executemany('''
# INSERT INTO statuses(name)
# VALUES(?);
# ''', ((('OUT OF STOCK', ), ('IN STOCK', ), ('PREORDER', ), ('FOR SALE', ))))
# conn.commit()


cur.execute('''
    CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    status_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(status_id) REFERENCES statuses(id)
    );
''')
conn.commit()
cur.executemany('''
INSERT INTO orders(user_id, status_id)
VALUES(?, ?);
''', ((1, 3), (2, 4), (3, 1)))
conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(24) NOT NULL UNIQUE
    );
''')
conn.commit()
# cur.executemany('''
# INSERT INTO categories(name)
# VALUES(?);
# ''', (('food',),('drinks', ), ('clothes',)))
# conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS products(
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(36) NOT NULL,
    descriptions VARCHAR(140),
    category_id INTEGER NOT NULL,
    FOREIGN KEY(category_id) REFERENCES categories(id)
    );
''')
conn.commit()
# cur.executemany('''
# INSERT INTO products(title, descriptions, category_id)
# VALUES(?, ?, ?);
# ''', (('bread', 'from flower', 1), ('water', 'with lemon flavor', 2), ('skirt', 'navy-black', 3)))
# conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS order_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY(order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY(product_id) REFERENCES products(id)
    );
''')
conn.commit()
# cur.executemany('''
# INSERT INTO order_items(order_id, product_id)
# VALUES(?, ?);
# ''', (()))



