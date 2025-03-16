from flask import Flask, render_template, request, jsonify
import pickle
import os
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model/ipl_win_predictor.pkl", "rb"))

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = [float(request.form[key]) for key in request.form.keys()]
        data = np.array(data).reshape(1, -1)
        
        # Predict probability
        prediction = model.predict_proba(data)[0][1]  # Probability of winning
        
        return jsonify({'win_probability': round(prediction * 100, 2)})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
