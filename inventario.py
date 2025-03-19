import sqlite3
conn = sqlite3.connect('inventario.db')
cursor = conn.cursor()
cursor.execute('''
 CREATE TABLE IF NOT EXISTS productos (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 nombre TEXT NOT NULL,
 categoria TEXT,
 cantidad INTEGER NOT NULL,
 precio REAL NOT NULL
 )
''')
conn.commit()
conn.close() 

