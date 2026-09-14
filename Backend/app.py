from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_connection():
    return sqlite3.connect("road_damage.db")

@app.route("/")
def home():
    return "Road Damage Detection Backend is Running!"

@app.route("/damage")
def get_damage():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM damage")
    rows = cursor.fetchall()

    connection.close()

    damage_list = []

    for row in rows:
        damage_list.append({
            "id": row[0],
            "damage_type": row[1],
            "severity": row[2],
            "latitude": row[3],
            "longitude": row[4],
            "priority": row[5],
            "estimated_cost": row[6]
        })

    return jsonify(damage_list)

if __name__ == "__main__":
    app.run(debug=True)
