import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np

# Load pretrained model
model = MobileNetV2(weights='imagenet')

# Corrections for known mismatches
corrections = {
    "consomme": "Dosa",
    "pancake": "Dosa",
    "soup": "Rasam",
    "fritters": "Vada",
    "bakery": "Idli",
    "omelet": "Uttapam",
    "spaghetti_squash": "Upma",
    "potpie": "Curry",
    "meatloaf": "Cutlet"
}

def predict_food(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = preprocess_input(np.expand_dims(image.img_to_array(img), axis=0))
    preds = model.predict(x)
    predicted_label = decode_predictions(preds, top=1)[0][0][1]
    return corrections.get(predicted_label.lower(), predicted_label)
