import tensorflow as tf
# from keras.preprocessing import image
import numpy as np
# import tensorflow as tf
from tensorflow import keras
from PIL import Image
from collections import Counter
# tf.disable_v2_behavior()
# import keras
import os

# Assuming your model is already loaded and named 'cnn'
def predict_raga(img_path):
    # img_path = 'test_raga'
    print("HIHIHI")
    # Initialize an empty list to store preprocessed images
    batch_images = []
    ragas = ['Aaberi', 'Aanandha bairavi', 'Bilahari', 'Chakravaakam', 'Dharbaarikaanada', 'Hamsadhwani', 'Harikaamboji', 'Hindolam', 'Joog', 'Kaapi', 'Kalyani', 'Kharaharapriya', 'Madhyamaavathi', 'Mohanam', 'Shankaraabharanam', 'Shanmuka priya', 'Shivaranjini', 'Shudhadhanyasi', 'Sindhu bairavi', 'Vrindhaavana saaranga', 'Yamuna kalyani']
    dictionary = {}
    custom_optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

    # Iterate through images in the folder
    for imgfile in os.listdir(img_path):
        img_path_full = os.path.join(img_path, imgfile)

        # Load and preprocess each image
        img = Image.open(img_path_full).resize((120, 120))
        img = img.convert("RGB")
        img_array = np.array(img) / 255.0  # Normalize to [0, 1]
        batch_images.append(img_array)

    # Convert the list of images to a numpy array
    batch_images = np.array(batch_images)
    # model = tf.keras.models.load_model('/content/drive/MyDrive/raga.h5', custom_objects={'Adam': custom_optimizer})
    # Make predictions for the entire batch
    model = keras.models.load_model(os.path.abspath(os.getcwd()) + "\\model\\raga.h5")

    predictions = model.predict(batch_images)
    # print(predictions)
    arr = []
    # # # Print the predictions
    # # print(np.argmax(predictions))
    # # # print(ragas[np.argmax(predictions)])
    for i in predictions:
        arr.append(np.argmax(i))
        # print(np.argmax(i), ragas[np.argmax(i)], end=" ")
        # print()

    counter = Counter(arr)

    most_common, most_count = counter.most_common(1)[0]
    for i in arr:
        try:
            dictionary[ragas[i]] += 1
        except:
            dictionary[ragas[i]] = 1
    # Return the most common element
    print(arr)
    print( dictionary) 
    return ragas[most_common]