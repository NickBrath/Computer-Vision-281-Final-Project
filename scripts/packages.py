# base packages
import os
import warnings
from datetime import date

from tqdm.notebook import tqdm  # progress bar library
# import glob
# import re
# import random

# DS packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns

# %matplotlib inline

# image packages
import PIL
import urllib
import cv2
from skimage.color import rgb2gray
import skimage.io as skio
import tabulate

# ML packages
import scipy as sc
import sklearn as sk
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Conv2D, Flatten, Dense, Dropout, MaxPooling2D, BatchNormalization
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.metrics import Accuracy,binary_crossentropy, FalsePositives, FalseNegatives, TruePositives, TrueNegatives
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.metrics import confusion_matrix, classification_report


import tomopy
import mkl
# Intel(R) MKL FFT functions to run sequentially
mkl.domain_set_num_threads(1, domain='fft')


# options
pd.options.display.max_columns = 50
warnings.filterwarnings("ignore")

og_cmap = plt.get_cmap(name=None, lut=None)

# Google packages
# from google.colab import drive
# from google.colab import files
# from google.colab.patches import cv2_imshow

# Mount google drive
# drive.mount('/content/drive')
