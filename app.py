from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Isse frontend aur backend connect honge

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'status': 'No image uploaded'}), 400
        
    file = request.files['image']
    if file.filename == '':
        return jsonify({'status': 'No selected file'}), 400

    # Test karne ke liye dummy result bhej rahe hain
    detection_result = "Pothole Detected" 
    return jsonify({'status': detection_result})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
  
