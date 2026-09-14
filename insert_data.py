import sqlite3

connection = sqlite3.connect("road_damage.db")
cursor = connection.cursor()

cursor.execute("""
INSERT INTO damage
(damage_type, severity, latitude, longitude, priority, estimated_cost)
VALUES (?, ?, ?, ?, ?, ?)
""", ("Pothole", "High", 17.3850, 78.4867, "High", 5000))

connection.commit()
connection.close()

print("Sample damage data inserted successfully!")
