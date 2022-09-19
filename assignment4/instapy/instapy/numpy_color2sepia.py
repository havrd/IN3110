import cv2
import numpy as np


def sepia_filter(filename, step=1.0):
    """
        Sepia filter for images, implemented with numpy
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

    sepia_matrix = np.matrix([[ 0.272 - 0.272 * (1 - step), 0.534 - 0.534* (1 - step), 0.131 + 0.869 * (1 - step)],
    [ 0.349 - 0.349 * (1 - step), 0.686 + 0.314 * (1 - step), 0.168 - 0.168 * (1 - step)],
    [ 0.393 + 0.607 * (1 - step), 0.769 - 0.769 * (1 - step), 0.189 - 0.189 * (1 - step)]])

    image = np.array([x * sepia_matrix.T for x in image])
    image[np.where(image>255)] = 255

    image = image.astype("uint8")
    temp = filename.split(".")
    new_filename = temp[0] + "_sepia.jpeg"
    cv2.imwrite(new_filename, image)

sepia_filter("rain.jpeg")
