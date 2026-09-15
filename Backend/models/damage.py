def create_damage_table(connection):
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

def insert_damage(connection, damage_type, severity, latitude, longitude, priority, estimated_cost):
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO damage (damage_type, severity, latitude, longitude, priority, estimated_cost)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (damage_type, severity, latitude, longitude, priority, estimated_cost))
    connection.commit()
