import sqlite3 

conn = sqlite3.connect('concerts.db')  

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS bands (
        id INTEGER PRIMARY KEY,
        name TEXT,
        hometown TEXT
    );
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS venues (
        id INTEGER PRIMARY KEY,
        title TEXT,
        city TEXT
    );
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS concerts (
        id INTEGER PRIMARY KEY,
        band_id INTEGER,
        venue_id INTEGER,
        date STRING,
        FOREIGN KEY (band_id) REFERENCES bands(id) ON DELETE CASCADE,
        FOREIGN KEY (venue_id) REFERENCES venues(id) ON DELETE CASCADE
    );
''')

conn.commit()
