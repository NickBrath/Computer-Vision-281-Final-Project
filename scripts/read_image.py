import tensorflow as tf

def read_image2(image_file_path, label):
    """Function to read in images to create tf dataset. Adds an extra dimension for batch. Allows use on sobel filter. """
    
    image = tf.io.read_file(image_file_path)  # read in image
    
    # preserving RGB colors with channels = 3. Reads array
    image = tf.image.decode_image(image, channels=3, dtype=tf.float32)
    
    # add batch dimension
    image = image[tf.newaxis, :]

    return image, label