import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import os
from tensorflow.keras.preprocessing.image import save_img


def resize_img(path, shape = 128):
    img = plt.imread(path)
    resized_img = cv2.resize(img, (shape, shape))
    return resized_img

def convert_to_tensor(img):
    resized_img = img[None, ...]
    return resized_img

def predict(tensor, model):
    output = model.predict(tensor)
    return output

def squeeze_img(img):
    img = np.squeeze(img, 0)
    img = np.squeeze(img, 2)
    return img

def get_result(img_path, model):
    img = resize_img(img_path)
    tensor = convert_to_tensor(img)
    output = predict(tensor, model)
    result = squeeze_img(output)
    return result

def save_result(write_path, img):
    final_result = tf.keras.preprocessing.image.img_to_array(img)
    save_img(write_path, final_result)

def process_image(upload_directory, result_directory, file_name):

    unet_model = tf.keras.models.load_model('cnn_model/route_generator_weights.h5')

    read_path = upload_directory + file_name
    print(read_path)

    result = get_result(read_path, unet_model)

    if not os.path.exists(result_directory):
        os.mkdir(result_directory)

    write_path = result_directory + file_name

    save_result(write_path, result)

