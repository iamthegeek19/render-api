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
    model = tf.keras.models.load_model('native_model')
    model.summary()

if __name__ == '__main__':
    app.run()