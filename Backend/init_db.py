import sqlite3

connection = sqlite3.connect("road_damage.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS damage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    damage_type TEXT,
    severity TEXT,
    latitude REAL,
    longitude REAL,
    priority TEXT,
    estimated_cost REAL
)
""")

connection.commit()
connection.close()

print("Database and damage table created successfully!")
