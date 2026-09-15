from flask import Flask, jsonify
from controllers.damage_controller import get_damage_data

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Road Damage Detection Backend Running!"

@app.route("/damage", methods=["GET"])
def damage():
    data = get_damage_data()
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True)
