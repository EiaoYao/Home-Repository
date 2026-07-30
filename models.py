python

import sqlite3

def init_db():

conn = sqlite3.connect('inventory.db')

c = conn.cursor()

c.execute('''

CREATE TABLE IF NOT EXISTS items (

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT NOT NULL,

category TEXT,

quantity INTEGER DEFAULT 1,

location TEXT

)

''')

conn.commit()
