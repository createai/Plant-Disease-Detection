import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Lambda
from keras.optimizers import Adam
from keras.layers.normalization import BatchNormalization
from keras.utils import np_utils
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D, GlobalAveragePooling2D
from keras.layers.advanced_activations import LeakyReLU 
from keras.preprocessing.image import ImageDataGenerator
from glob import glob
from shutil import copyfile
from PIL import Image

def create_model():
	mean_sub = np.array([123.68, 116.779, 103.939], dtype=np.float32)
	pre_processing = lambda x: (x - mean_sub)[:,:,:,::-1]


	model = Sequential()

	model.add(Lambda(pre_processing, input_shape=(224,224,3), 
	                 output_shape=(224,224,3)))

	model.add(ZeroPadding2D((1, 1)))
	model.add(Convolution2D(64, 3, 3, activation='relu', name='conv1_1'))
	model.add(ZeroPadding2D((1, 1)))
	model.add(Convolution2D(64, 3, 3, activation='relu', name='conv1_2'))
	model.add(MaxPooling2D((2, 2), strides=(2, 2)))

	model.add(ZeroPadding2D((1, 1)))
	model.add(Convolution2D(128, 3, 3, activation='relu', name='conv2_1'))
	model.add(ZeroPadding2D((1, 1)))
	model.add(Convolution2D(128, 3, 3, activation='relu', name='conv2_2'))
	model.add(MaxPooling2D((2, 2), strides=(2, 2)))

	model.add(ZeroPadding2D((1, 1)))
	model.add(Convolution2D(256, 3, 3, activation='relu', name='conv3_1'))
	model.add(ZeroPadding2D((1, 1)))
	model.add(Convolution2D(256, 3, 3, activation='relu', name='conv3_2'))
	model.add(ZeroPadding2D((1, 1)))
	model.add(Convolution2D(256, 3, 3, activation='relu', name='conv3_3'))
	model.add(MaxPooling2D((2, 2), strides=(2, 2)))

	model.add(ZeroPadding2D((1, 1)))
	model.add(Convolution2D(512, 3, 3, activation='relu', name='conv4_1'))
	model.add(ZeroPadding2D((1, 1)))
	model.add(Convolution2D(512, 3, 3, activation='relu', name='conv4_2'))
	model.add(ZeroPadding2D((1, 1)))
	model.add(Convolution2D(512, 3, 3, activation='relu', name='conv4_3'))
	model.add(MaxPooling2D((2, 2), strides=(2, 2)))

	model.add(ZeroPadding2D((1, 1)))
	model.add(Convolution2D(512, 3, 3, activation='relu', name='conv5_1'))
	model.add(ZeroPadding2D((1, 1)))
	model.add(Convolution2D(512, 3, 3, activation='relu', name='conv5_2'))
	model.add(ZeroPadding2D((1, 1)))
	model.add(Convolution2D(512, 3, 3, activation='relu', name='conv5_3'))
	model.add(MaxPooling2D((2, 2), strides=(2, 2)))

	model.add(Flatten())
	model.add(Dense(4096, activation='relu'))
	model.add(Dropout(0.5))
	model.add(Dense(4096, activation='relu'))
	model.add(Dropout(0.5))

	model.add(Dense(4, activation='softmax'))

	model.load_weights('vgg_plant.h5')

	model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

	return model



















