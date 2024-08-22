from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the model
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse the form data
        material_id = request.form['material_id']
        standard_lead_time = float(request.form['standard_lead_time'])
        quantity = float(request.form['quantity'])
        price = float(request.form['price'])

        # Prepare data for prediction
        new_data = pd.DataFrame({
            'Material_Id': [material_id],
            'Standard_Lead_Time': [standard_lead_time],
            'Quantity': [quantity],
            'Price': [price]
        })

        # Make predictions
        predictions = model.predict(new_data)

        # Decode the predicted Vendor_Id back to original format
        predicted_vendor_id = int(np.round(predictions[0, 0]))
        predicted_lead_time = predictions[0, 1]

        return jsonify({
            'Predicted_Vendor_Id': predicted_vendor_id,
            'Predicted_Lead_Time': predicted_lead_time
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
