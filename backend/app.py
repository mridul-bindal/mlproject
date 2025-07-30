from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the ML model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return '✅ Flask server is running with ML model!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    features = data.get('features')

    if not features or not isinstance(features, list) or len(features) != 7:
        return jsonify({'error': 'Expected 7 numerical features in a list'}), 400

    try:
        features_array = np.array([features])
        prediction = model.predict(features_array)[0]
        return jsonify({'prediction': str(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
