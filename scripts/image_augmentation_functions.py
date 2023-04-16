import tensorflow as tf

def create_image_set(ds, num_images = 5): 
    # create preview of images with labels
    images = []
    for i, t in enumerate(ds.take(num_images)): 
        images.append(
            {'label': tf.argmax(t[1].numpy()).numpy(), 
            'im' : t[0].numpy()}
        )

    return images


def augment_grayscale(image, label):
    # turn image from RGB to grayscale
    if tf.random.uniform((), minval=0, maxval=1) < 0.1:
        image = tf.tile(tf.image(tf.image.rgb_to_grayscale(image), [1, 1, 3]))
    
    return image, label

## Basic Augmentations

# image sharpening
def augment_sharpen(image, label): 
    
    # image sharpening
    
    return image, label


def augment_contrast(image, label): 
    """ Adjust contrast of image """
    
    image = tf.image.random_contrast(image, lower=0.1, upper=0.5)
    
    return image, label

def augment_normalize(image, label):
    """ Normalize images for pixel intensity variations to gaussian distribution"""
    
    return tf.cast(image, tf.float32) / 255.0, label

def augment_rotation(image, label): 
    """ Apply a random rotation """
    
    image = tf.keras.preprocessing.image.random_rotation(image)
    
    return image, label

def augment_brightness(image, label): 
    """ Change image brightness on pixels a random amount """
    image = tf.image.random_brightness(image, max_delta=0.1)
    
    return image, label

def augment_flip(image,label):
    """ horizontal and vertically flip images"""
    image = tf.image.random_flip_left_right(image)  # 50%
    image = tf.image.random_flip_up_down(image)
    
    return image, label

def augment_centralcrop(image, label): 
    """take image and return fraction of the image cropped centered"""
    # needs work
    image = tf.image.central_crop(image, 0.5)
    
    return image, label

def augment_crop(image, label, size = 120): 
    """ Crops image by defining a bounding box
    
    Using to make sure the images are the same size.     
    """
    # normalize image size to a square and get smaller subsection
    offsetwidth = offsetheight = size
    image = tf.image.crop_to_bounding_box(image, 0, 0, offsetwidth, offsetheight)
    
    return image, label

## Advanced augmentations

def augment_sobel_edges(image, label): 
    """ Apply the sobel-edge dector function over tensors"""
    image = tf.image.sobel_edges(image)
    
    return image, label

def augment_patches(image, label): 
    """ Get patches of image like a convolution"""
    #### Random sample 32, 32, 3 like they do in the paper
    
    image = tf.image.extract_patches(
        images=image,
        sizes=[1, 32, 32, 1],
        strides=[1, 16, 16, 1],
        rates=[1, 1, 1, 1],
        padding='VALID'
        )
    
    return image, label

def augment(image, label):
    # data augmentation here
    # is done while the model is training
    # did it this way to change which augmentations are applied. Thought it would be easier to break down functions into parts. 

    # image, label = augment_normalize(image,label)
    
    image, label = augment_resize(image,label)
    
    image, label = augment_grayscale(image,label)
    
    image, label = augment_sharpen(image,label)
    
    image, label = augment_brightness(image,label)
    
    image, label = augment_contrast(image,label)
    
    image, label = augment_flip(image,label)
   
    return image, label



### Histogram Equalization Contrast
def histogram_equalization(im):
  img_cdf, bins = exposure.cumulative_distribution(im, 256)
  container = np.zeros(256)
  container[bins] = img_cdf
  holding_image = np.empty(im.shape)
  for i in range(im.shape[0]):
    for y in range(im.shape[1]):
      holding_image[i][y] = container[im[i][y]]
  equalized_image = holding_image
  equalized_image = img_as_ubyte(equalized_image) 
  return equalized_image


#needs work
def get_total_variation(image, label): 
    tv = tf.image.total_variation(image, name=None).numpy()
    
    return tv
