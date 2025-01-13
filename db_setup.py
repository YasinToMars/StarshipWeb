import sqlite3

conn = sqlite3.connect('contact.db')
cursor = conn.cursor()

# Create the contacts table
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Database created successfully.")