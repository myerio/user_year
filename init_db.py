import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    BirthYear INTEGER
)
""")

cursor.executemany("INSERT INTO Users (Name, BirthYear) VALUES (?, ?)", [
    ("John", 1995),
    ("Maria", 1997),
    ("Daniel", 1994),
    ("Mike", 1998),
    ("Rob", 2001)
])

conn.commit()
conn.close()
print("Database created and populated successfully.")