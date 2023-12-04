from tensorflow.keras.models import model_from_json
import numpy as np
from tensorflow.keras.preprocessing import image
import os

# Load model architecture from JSON file
json_file_path = os.path.join('C:\\Users\\91782\\OneDrive\\Desktop\\kushi ai', 'model.json')
h5_file_path = os.path.join('C:\\Users\\91782\\OneDrive\\Desktop\\kushi ai', 'model.h5')

with open(json_file_path, 'r') as json_file:
    loaded_model_json = json_file.read()

model = model_from_json(loaded_model_json)
model.load_weights(h5_file_path)
print("Loaded model from disk")

def classify(img_file):
    img_name = img_file
    try:
        test_image = image.load_img(img_name, target_size=(64, 64))
    except Exception as e:
        print(f"Error loading image {img_name}: {e}")
        return  # Skip to the next iteration

    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)

    prediction = 'acne' if result[0][0] == 1 else 'Rosacea'
    print(f"Prediction: {prediction}, Image Path: {os.path.abspath(img_name)}")

# Traverse the directory and classify images
path = 'Dataset\\test'
files = []

for r, d, f in os.walk(path):
    for file in f:
        _, file_extension = os.path.splitext(file)
        if file_extension.lower() == '.jpeg':
            files.append(os.path.join(r, file))

for f in files:
    classify(f)
    print('\n')
