import cv2
import numpy as np
from numba import jit


def greyscale_image(input_filename, output_filename=None, scale=None, implementation=None):
    """
        Greyscale filter for images
        Args:
            input_filename (string): filename of image to be filteres
            output_filename (string): filename for saving image, if None; image is not saved
            scale (float): scale image using a floating number where 1.0 is original size
            implementation (string): select implementation
        Returns:
            numpy ndarray (3D) containing an image.
    """
    image = cv2.imread(input_filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if scale != None:
        if scale <= 0: scale = 0.01
        image = cv2.resize(image, (0,0), fx=scale, fy=scale)

    # Python-implementation
    if implementation == "python":
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

    # Numba-implementation
    elif implementation == "numba":
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

    # Numpy-implementation
    else:
        r,g,b = image[:,:,0], image[:,:,1], image[:,:,2]
        sum = r*0.21 + g*0.72 + b*0.07
        image[:,:,0] = image[:,:,1] = image[:,:,2] = sum

    # Convert values in image from float to uint8
    image = image.astype("uint8")
    if output_filename != None:
        new_filename = str(output_filename) + ".jpeg"
        cv2.imwrite(new_filename, image)
    return image



def sepia_image(input_filename, output_filename=None, scale=None, implementation=None, step=1.0):
    """
        Sepia filter for images
        Args:
            input_filename (string): filename of image to be filteres
            output_filename (string): filename for saving image, if None; image is not saved
            scale (float): scale image using a floating number where 1.0 is original size
            implementation (string): select implementation
            step (float): intensity of sepia filter, 0.0 is no filter and 1.0 is maximum filter
        Returns:
            numpy ndarray (3D) containing an image.
    """
    image = cv2.imread(input_filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


    if step > 1.0: step = 1.0
    if step < 0: step = 0

    if scale != None:
        if scale <= 0: scale = 0.01
        image = cv2.resize(image, (0,0), fx=scale, fy=scale)

    # Python-implementation
    if implementation == "python":
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

    # Numba-implementation
    elif implementation == "numba":
        @jit(nopython=True)
        def loop(image):
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
            return image

        image = loop(image)

    # Numpy-implementation
    else:
        sepia_matrix = np.array([[ 0.272 - 0.272 * (1 - step), 0.534 - 0.534* (1 - step), 0.131 + 0.869 * (1 - step)],
        [ 0.349 - 0.349 * (1 - step), 0.686 + 0.314 * (1 - step), 0.168 - 0.168 * (1 - step)],
        [ 0.393 + 0.607 * (1 - step), 0.769 - 0.769 * (1 - step), 0.189 - 0.189 * (1 - step)]])

        image = np.dot(image, sepia_matrix.T) #Important to transpose matrix so that the correct axes are multiplied
        image[np.where(image>255)] = 255

    # Convert values in image from float to uint8
    image = image.astype("uint8")
    if output_filename != None:
        new_filename = str(output_filename) + ".jpeg"
        cv2.imwrite(new_filename, image)
    return image
