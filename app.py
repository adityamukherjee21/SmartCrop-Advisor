from flask import Flask, render_template, request
import pickle
import numpy as np
from collections import deque

app = Flask(__name__)

# ✅ Load your models here before you use them
dt_model = pickle.load(open('dt_model.pkl', 'rb'))
rf_model = pickle.load(open('rf_model.pkl', 'rb'))

history = deque(maxlen=5)

# Sample crop info dictionary (same as you have)
crop_info = {
    'rice': {'soil': 'Clayey, loamy', 'temperature': '20-30°C', 'region': 'Eastern & Southern India', 'season': 'Kharif'},
    'maize': {'soil': 'Well-drained alluvial', 'temperature': '21-27°C', 'region': 'Punjab, Bihar', 'season': 'Kharif'},
    'chickpea': {'soil': 'Loamy, well-drained', 'temperature': '25-30°C', 'region': 'Central & Western India', 'season': 'Rabi'},
    'kidneybeans': {'soil': 'Well-drained sandy loam', 'temperature': '20-25°C', 'region': 'North & Central India', 'season': 'Rabi'},
    'pigeonpeas': {'soil': 'Loamy, sandy', 'temperature': '25-30°C', 'region': 'Southern India', 'season': 'Kharif'},
    'mothbeans': {'soil': 'Sandy, well-drained', 'temperature': '30-40°C', 'region': 'Rajasthan, Gujarat', 'season': 'Kharif'},
    'mungbean': {'soil': 'Well-drained, sandy loam', 'temperature': '25-35°C', 'region': 'North & Central India', 'season': 'Kharif'},
    'blackgram': {'soil': 'Loamy, fertile', 'temperature': '25-30°C', 'region': 'Southern & Central India', 'season': 'Kharif'},
    'lentil': {'soil': 'Well-drained, loamy', 'temperature': '15-20°C', 'region': 'Northern India', 'season': 'Rabi'},
    'pomegranate': {'soil': 'Well-drained sandy, loamy', 'temperature': '30-35°C', 'region': 'Maharashtra, Andhra Pradesh', 'season': 'Post-monsoon'},
    'banana': {'soil': 'Well-drained, sandy loam', 'temperature': '25-30°C', 'region': 'Tamil Nadu, Kerala', 'season': 'All year round'},
    'mango': {'soil': 'Well-drained, sandy loam', 'temperature': '25-35°C', 'region': 'Maharashtra, Uttar Pradesh', 'season': 'Summer'},
    'grapes': {'soil': 'Well-drained, slightly acidic', 'temperature': '20-25°C', 'region': 'Maharashtra, Karnataka', 'season': 'Winter'},
    'watermelon': {'soil': 'Loamy, sandy', 'temperature': '25-30°C', 'region': 'Punjab, Rajasthan', 'season': 'Summer'},
    'muskmelon': {'soil': 'Loamy, well-drained', 'temperature': '25-35°C', 'region': 'North India', 'season': 'Summer'},
    'apple': {'soil': 'Well-drained, loamy', 'temperature': '10-20°C', 'region': 'Jammu & Kashmir', 'season': 'Autumn'},
    'orange': {'soil': 'Loamy, well-drained', 'temperature': '25-35°C', 'region': 'Maharashtra, Gujarat', 'season': 'Winter'},
    'papaya': {'soil': 'Sandy loam, well-drained', 'temperature': '25-30°C', 'region': 'Kerala, Tamil Nadu', 'season': 'All year round'},
    'coconut': {'soil': 'Sandy loam, well-drained', 'temperature': '25-30°C', 'region': 'Kerala, Tamil Nadu', 'season': 'All year round'},
    'cotton': {'soil': 'Loamy, well-drained', 'temperature': '25-30°C', 'region': 'Maharashtra, Gujarat', 'season': 'Kharif'},
    'jute': {'soil': 'Silty loam, well-drained', 'temperature': '30-35°C', 'region': 'West Bengal, Bihar', 'season': 'Kharif'},
    'coffee': {'soil': 'Well-drained, rich in organic matter', 'temperature': '18-25°C', 'region': 'Karnataka, Kerala', 'season': 'Monsoon'}
}


# Crop list for prediction
crop_list = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans',
             'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango',
             'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya',
             'coconut', 'cotton', 'jute', 'coffee']

crop_list = list(crop_info.keys())
history = deque(maxlen=5)

@app.route('/')
def index():
    return render_template('index.html', result=None, history=list(history), crops=[{'name': c} for c in crop_list])


@app.route('/predict', methods=['POST'])
def predict():
    # Get user input
    N = float(request.form['N'])
    P = float(request.form['P'])
    K = float(request.form['K'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])

    # Predict crop
    input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
    prediction = rf_model.predict(input_data)[0]  # or dt_model.predict(...)


    # Get details for predicted crop
    details = crop_info.get(prediction, {
        'soil': 'NA', 'season': 'NA', 'temperature': 'NA'
    })

    # Store in history with full details
    history.append({
        'crop': prediction,
        'soil': details['soil'],
        'season': details['season'],
        'climate': details['temperature']
    })

    return render_template('index.html',
                           result=prediction,
                           details=details,
                           history=list(history),
                           crops=[{'name': c} for c in crop_list])

if __name__ == '__main__':
    app.run(debug=True)
