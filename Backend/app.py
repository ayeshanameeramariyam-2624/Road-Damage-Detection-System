from flask import Flask
from controllers.damage_controller import damage_controller

app = Flask(__name__)

app.register_blueprint(damage_controller)

@app.route("/")
def home():
    return "AI Road Damage Detection Backend Running!"

if __name__ == "__main__":
    app.run(debug=True)
