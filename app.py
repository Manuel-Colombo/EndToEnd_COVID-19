from flask import Flask, request, jsonify
import joblib
import numpy as np
import sklearn  

app = Flask(__name__)

import os
print("User running the Flask app:", os.geteuid())


try:
    rf_model = joblib.load('model_rf.pkl')
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading the model: {e}")
    rf_model = None

def predict(model, data):
    if model:
        prediction = model.predict(data)
        return prediction.tolist()
    else:
        return None

@app.route('/predict_rf', methods=['POST'])
def predict_rf():
    if rf_model is None:
        return jsonify({'error': 'Model not loaded properly'}), 500
    
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = predict(rf_model, features)
    
    if prediction is None:
        return jsonify({'error': 'Prediction failed'}), 500

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True, port=5051)
