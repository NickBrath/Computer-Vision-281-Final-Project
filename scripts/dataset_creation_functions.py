def create_tf_ds(file_paths, labels):
    """ Create tensorflow dataset from file paths and labels """
    # create dataset
    ds = tf.data.Dataset.from_tensor_slices(
        (file_paths, labels))  # mapping like a zip in python

    return ds

def read_image(image_file_path, label):
    """Function to read in images to create tf dataset"""
    
    image = tf.io.read_file(image_file_path)  # read in image
    
    # preserving RGB colors with channels = 3. Reads array
    image = tf.image.decode_image(image, channels=3, dtype=tf.float64)

    return image, label


## Label encoding
# convert labels to numeric representation
from sklearn.preprocessing import LabelEncoder

# create encoder
labelencoder = LabelEncoder()

file_paths = df['FULL_PATH'].values
# using subtype of tumor labels as labels to get 8 different labels. Could use 'TUMOR_CLASS' if you want binary classification problem.

labels = df['TUMOR_TYPE'].values

## One-hot encoding for labels
# number of categories
depth = len(set(labels))

# apply encoder to change string labels to integer
labels_encoded = labelencoder.fit_transform(labels)

# One-hot encodning to feed into model(s)
labels = tf.one_hot(labels_encoded, depth=depth)

# create dataset (ds)
ds = create_tf_ds(file_paths, labels)


def decode_labels(labels_encoded): 
    # get labels back out
    return labelencoder.inverse_transform(labels_encoded)


def one_hot_argmax(label): 
    """ Getting the max value will help to decode since we have a 1 x 8 array size"""
    return tf.argmax(label, axis=0).numpy()

# test_label = one_hot_argmax(test_label)
# test_label = np.array(test_label)