def create_image_set(ds, num_images = 5): 
    # create preview of images with labels
    images = []
    for i, t in enumerate(ds.take(num_images)): 
        images.append(
            {'label': tf.argmax(t[1].numpy()).numpy(), 
            'im' : t[0].numpy()}
        )

    return images

def plot_sobel_images(images, nrows, ncols = 2): 
    """ List of image dictionaries with label: value, im: array
    Plots the sobel filter applied to an image side by side for the vertical and horizontal edges. 
    
    """

    fig, axs = plt.subplots(nrows, ncols, figsize=(5, 10))
    
    def squeeze_3d(image, title=None):
        """ Show image from tensor"""
        if len(image.shape) > 3:
            image = tf.squeeze(image, axis=0)
        return image

    for i, im in enumerate(images):
        # set label for the graph
        label = str(im['label'])
        
        # extract image array
        im = im['im']
        
        # two, one for the horizontal and vertical sobel edges
        for j in range(2): 
            # add image to axes            
            axs[i,j].imshow(squeeze_3d(im[..., j]/4+0.5))
            
            # drop axis labels
            axs[i,j].axis('off')
            
            # add axes title
            if j ==  0: 
                title = 'Horizontal'
            else: 
                title = 'Vertical'
                
            axs[i,j].set(title="-".join([label,title]))
        
    fig.suptitle("Sample of Sobel-edges", fontsize=16)

    plt.show()