import cv2


def sepia_filter(filename, step=1.0):
    """
        Sepia filter for images, implemented with pure python
        Args:
            filename (string): filename of image to be filteres
            step (float): intensity of sepia filter, 0.0 is no filter and 1.0 is maximum filter
        Returns:
            writes an imagefile in format <original_filename>_sepia.jpeg
    """
    image = cv2.imread(filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if step>1.0: step = 1.0
    if step<0: step = 0

    rows, cols, pix = image.shape
    for width in range(rows):
        for height in range(cols):
            r = image[width][height][0]*(0.272-0.272*(1 - step)) + image[width][height][1]*(0.534-0.534*(1 - step)) + image[width][height][2]*(0.131+0.869 *(1 - step))
            g = image[width][height][0]*(0.349-0.349*(1 - step)) + image[width][height][1]*(0.686+0.314*(1 - step)) + image[width][height][2]*(0.168-0.168*(1 - step))
            b = image[width][height][0]*(0.393+0.607*(1 - step)) + image[width][height][1]*(0.769-0.769*(1 - step)) + image[width][height][2]*(0.189-0.189*(1 - step))
            if r > 255: r = 255
            if g > 255: g = 255
            if b > 255: b = 255
            image[width][height][0] = r
            image[width][height][1] = g
            image[width][height][2] = b
    image = image.astype("uint8")
    temp = filename.split(".")
    new_filename = temp[0] + "_sepia.jpeg"
    cv2.imwrite(new_filename, image)

sepia_filter("rain.jpeg")
