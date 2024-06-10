from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model = load_model('tuberculosis (1).h5')

# Ensure the 'uploads' directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Define a function to prepare the image
def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # normalize to [0, 1] range
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('index.html', result_message='No file uploaded')
    
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', result_message='No file selected')

    # Save the file
    filepath = os.path.join('uploads', file.filename)
    file.save(filepath)

    # Prepare the image
    img_array = prepare_image(filepath)

    # Make prediction
    prediction = model.predict(img_array)
    prediction_label = 'positive' if prediction[0][0] > 0.5 else 'normal'

    # Remove the file after prediction
    os.remove(filepath)

    # Render the result on the results page
    return render_template('result.html', result_message=prediction_label)

if __name__ == '__main__':
    app.run(debug=True)
