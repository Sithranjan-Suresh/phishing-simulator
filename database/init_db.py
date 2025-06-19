# database/init_db.py
import sqlite3
from datetime import datetime

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS clicks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    target TEXT,
    timestamp TEXT
)
''')

conn.commit()
conn.close()
print("✅ Database initialized.")
