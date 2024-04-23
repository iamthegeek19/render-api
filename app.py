# ### IMPORTS
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import Sequential, layers
from tensorflow.keras.optimizers import Adam
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users')
def vanhu():
    users = {
        'name': 'donty',
        'name1': 'hussein',
        'name3': 'hameno'
    }
    return users

@app.route('/model')
def deploy():
    ### Preparing the dataset

    data_dir = './Faulty_solar_panel/'

    directory = './Faulty_solar_panel/'
    image_size = (224,224)
    batch_size = 32

    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        directory,
        label_mode='categorical',
        validation_split=0.2,
        subset="training",
        seed=42,
        image_size=image_size,
        batch_size=batch_size,
    )
    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        directory,
        validation_split=0.2,
        subset="validation",
        label_mode='categorical',
        seed=42,
        image_size=image_size,
        batch_size=batch_size,
    )

    class_names = train_ds.class_names
    return {'class_names': class_names}
    # ### Loading the model
    # model = tf.keras.models.load_model('native_model')
    # res = model.evaluate(val_ds)

if __name__ == '__main__':
    app.run()