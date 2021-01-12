import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import glob
import os


# function to extract the file name from file path
def get_name(path):
    photo_name = path.split('\\')[-1]
    return photo_name


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model from teachablemachine
model = tensorflow.keras.models.load_model(r"tensorflow\keras_model.h5")

# Get all files
photos_path = glob.glob(r"D:\PycharmProjects\Review\image_classification\images\*.jpg")
dest_path = r"D:\PycharmProjects\Review\image_classification\images"

# Create the array of the right shape to feed into the keras model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# loop to read and move all photos
for photo in photos_path:
    # image path
    image = Image.open(photo)

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    # image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # create the prediction
    prediction = model.predict(data)
    img_name = get_name(photo)

    # move photo to folder
    # homem
    if prediction[0][0] == max(prediction[0]) and prediction[0][0] >= 0.5:
        os.rename(photo, dest_path + "\\" + r'homem\{}'.format(img_name))
        print(img_name, ' homem: {:.2f}%'.format(prediction[0][0]*100))
    # mulher
    elif prediction[0][1] == max(prediction[0]) and prediction[0][1] >= 0.5:
        os.rename(photo, dest_path + "\\" + r'mulher\{}'.format(img_name))
        print(img_name, ' mulher: {:.2f}%'.format(prediction[0][1]*100))
    # outros
    elif prediction[0][2] == max(prediction[0]) and prediction[0][2] >= 0.5:
        os.rename(photo, dest_path + "\\" + r'kid\{}'.format(img_name))
        print(img_name, ' kid: {:.2f}%'.format(prediction[0][2]*100))
    # error or confidence < 50%
    else:
        print('Ignorou ', img_name)

