import cv2
from numba import jit



def greyscale_filter(filename):
    """
        Greyscale filter for images, implemented with numba
        Args:
            filename (string): filename of image to be filteres
        Returns:
            writes an imagefile in format <original_filename>_greyscale.jpeg
    """
    image = cv2.imread(filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    @jit(nopython=True)
    def loop(image):
        rows, cols, pix = image.shape
        for width in range(rows):
            for height in range(cols):
                r = image[width][height][0] * 0.21
                g = image[width][height][1] * 0.72
                b = image[width][height][2] * 0.07
                sum = r+g+b
                image[width][height][0] = sum
                image[width][height][1] = sum
                image[width][height][2] = sum
        return image

    image = loop(image);
    image = image.astype("uint8")
    temp = filename.split(".")
    new_filename = temp[0] + "_greyscale.jpeg"
    cv2.imwrite(new_filename, image)

greyscale_filter("rain.jpeg")
