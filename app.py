from flask import Flask, render_template, request, jsonify
from keras.models import load_model
import numpy as np
from PIL import Image
import io
import base64

app = Flask(__name__)

model = load_model('model.weights.best.keras')
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    
    img_bytes = file.read()
    img = Image.open(io.BytesIO(img_bytes))
    img = img.resize((224, 224)) 
    img = np.array(img)
    img = img / 255.0 

    prediction = model.predict(np.expand_dims(img, axis=0))

    predicted_class = np.argmax(prediction)
    leaf_class = ['Damage Belt', 'Normal Belt']
    class_name = leaf_class[predicted_class]

    img_str = base64.b64encode(img_bytes).decode('utf-8')
    
    return jsonify({'prediction': class_name, 'image': img_str})

if __name__ == '__main__':
    app.run(debug=True)
