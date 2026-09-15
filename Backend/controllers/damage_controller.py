from flask import Blueprint, jsonify
from models.database import get_connection

damage_controller = Blueprint("damage_controller", __name__)

@damage_controller.route("/damage", methods=["GET"])
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
