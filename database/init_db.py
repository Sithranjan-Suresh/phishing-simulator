# database/init_db.py
import sqlite3
from datetime import datetime

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Clicks table (already exists)
c.execute('''
CREATE TABLE IF NOT EXISTS clicks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    target TEXT,
    timestamp TEXT
)
''')

# NEW: Credentials table
c.execute('''
CREATE TABLE IF NOT EXISTS credentials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    timestamp TEXT
)
''')

conn.commit()
conn.close()
print("✅ Database and tables initialized.")
