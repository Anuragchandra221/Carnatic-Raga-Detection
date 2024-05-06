import tensorflow as tf
import numpy as np
from tensorflow import keras
from PIL import Image
from program import find_consec
from collections import Counter
import os
def predict_raga(img_path):
    print("HIHIHI")
    batch_images = []
    ragas = ['Aaberi', 'Aanandha bairavi', 'Bilahari', 'Chakravaakam', 'Dharbaarikaanada', 'Hamsadhwani', 'Harikaamboji', 'Hindolam', 'Joog', 'Kaapi', 'Kalyani', 'Kharaharapriya', 'Madhyamaavathi', 'Mohanam', 'Shankaraabharanam', 'Shanmuka priya', 'Shivaranjini', 'Shudhadhanyasi', 'Sindhu bairavi', 'Vrindhaavana saaranga', 'Yamuna kalyani']
    dictionary = {}
    custom_optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
    # Iterate through images in the folder
    for imgfile in os.listdir(img_path):
        img_path_full = os.path.join(img_path, imgfile)
        img = Image.open(img_path_full).resize((120, 120))
        img = img.convert("RGB")
        img_array = np.array(img) / 255.0  # Normalize to [0, 1]
        batch_images.append(img_array)
    batch_images = np.array(batch_images)
    model = keras.models.load_model(os.path.abspath(os.getcwd()) + "\\model\\raga.h5")
    predictions = model.predict(batch_images)
    arr = []
    for i in predictions:
        arr.append(np.argmax(i))
    counter = Counter(arr)
    most_common, most_count = counter.most_common(1)[0]
    for i in arr:
        try:
            dictionary[ragas[i]] += 1
        except:
            dictionary[ragas[i]] = 1
    dictionary = find_consec(most_common, arr)
    print(arr)
    print(dictionary)
    return ragas[most_common]