import os
import numpy as np
from flask import Flask, request, render_template, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

app = Flask(__name__)

# Set the upload folder and allowed file extensions
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}

# Function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Load a pre-trained ResNet50 model
model = tf.keras.models.load_model('DenseNetApproach.h5')

disease_descriptions = {
    'Melanoma (MEL)': 'Melanoma is a type of skin cancer that arises from pigment-producing cells called melanocytes. It is often characterized by irregular moles or dark, asymmetrical growths on the skin.',
    'Melanocytic nevus (NV)': 'A melanocytic nevus, commonly known as a mole, is a benign growth on the skin. Moles are usually small, round, and can vary in color.',
    'Basal cell carcinoma (BCC)': 'Basal cell carcinoma is a common type of skin cancer that typically appears as a small, shiny bump or a red, scaly patch. It rarely spreads to other parts of the body.',
    'Actinic keratosis (AK)': 'Actinic keratosis, also known as solar keratosis, is a pre-cancerous skin condition caused by prolonged sun exposure. It often appears as rough, scaly patches on the skin.',
    'Benign keratosis (BKL)': 'Benign keratosis refers to non-cancerous growths on the skin. These growths can include seborrheic keratosis, which are often brown or black and have a waxy appearance.',
    'Dermatofibroma (DF)': 'Dermatofibroma is a benign skin tumor that usually appears as a small, brownish bump on the skin. It is often firm to the touch and may have a central dimple.',
    'Vascular lesion (VASC)': 'Vascular lesions refer to abnormalities in blood vessels. These can include conditions like hemangiomas and port-wine stains, which are characterized by red or purple discolorations on the skin.',
    'Squamous cell carcinoma (SCC)': 'Squamous cell carcinoma is a type of skin cancer that usually appears as a red, scaly patch or a firm, elevated growth. It can be more aggressive than basal cell carcinoma and may spread to other areas of the body.'
}



# Function to process the uploaded image and make predictions
def predict_image(file_path):
    img = image.load_img(file_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    predictions = model.predict(img_array)
    print(predictions)
    p=np.argmax(predictions)
    l=['Melanoma (MEL)',
    'Melanocytic nevus (NV)',
    'Basal cell carcinoma (BCC)',
    'Actinic keratosis (AK)',
    'Benign keratosis (BKL)',
    'Dermatofibroma (DF)', 
    'Vascular lesion (VASC)',
   'Squamous cell carcinoma (SCC)']
    decoded_prediction = l[p]
    
    return decoded_prediction

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file extension'})
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Process the uploaded image and make predictions
        prediction = [predict_image(file_path),disease_descriptions[predict_image(file_path)]]

        return render_template('ret.html', data=prediction)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
