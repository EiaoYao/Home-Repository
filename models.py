python

import sqlite3

from config import Config

def get_db_connection():

conn = sqlite3.connect(Config.DATABASE)

conn.row_factory = sqlite3.Row

return conn

def init_db():

conn = get_db_connection()

cursor = conn.cursor()

cursor.execute('''

CREATE TABLE IF NOT EXISTS item (

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT NOT NULL,

category TEXT,

quantity INTEGER DEFAULT 1,

location TEXT

)

''')

conn.commit()

conn.close()

def get_all_items():

conn = get_db_connection()

items = conn.execute('SELECT * FROM item').fetchall()

conn.close()

return items

def get_item_by_id(item_id):

conn = get_db_connection()

item = conn.execute('SELECT * FROM item WHERE id = ?', (item_id,)).fetchone()

conn.close()

return item

def add_item(name, category, quantity, location):

conn = get_db_connection()

conn.execute('INSERT INTO item (name, category, quantity, location) VALUES (?, ?, ?, ?)',

(name, category, quantity, location))

conn.commit()

conn.close()

def update_item(item_id, name, category, quantity, location):

conn = get_db_connection()

conn.execute('UPDATE item SET name = ?, category = ?, quantity = ?, location = ? WHERE id = ?',

(name, category, quantity, location, item_id))

conn.commit()

conn.close()

def delete_item(item_id):

conn = get_db_connection()

conn.execute('DELETE FROM item WHERE id = ?', (item_id,))

conn.commit()

conn.close()
