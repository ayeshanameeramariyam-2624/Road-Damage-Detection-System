from flask import Blueprint, jsonify, request
from algorithms.models.database import get_connection
from algorithms.priority import calculate_priority
from algorithms.cost_estimation import estimate_cost

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


@damage_controller.route("/damage", methods=["POST"])
def add_damage():

    data = request.get_json()

    damage_type = data.get("damage_type")
    severity = data.get("severity")
    latitude = data.get("latitude", 0)
    longitude = data.get("longitude", 0)

    priority = calculate_priority(severity)
    estimated_cost = estimate_cost(damage_type, severity)

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO damage
        (damage_type, severity, latitude, longitude, priority, estimated_cost)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        damage_type,
        severity,
        latitude,
        longitude,
        priority,
        estimated_cost
    ))

    connection.commit()
    connection.close()

    return jsonify({
        "message": "Damage record added successfully",
        "damage_type": damage_type,
        "severity": severity,
        "latitude": latitude,
        "longitude": longitude,
        "priority": priority,
        "estimated_cost": estimated_cost
    }), 201
