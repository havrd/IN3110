from instapy.image_filters import greyscale_image as gi
from instapy.image_filters import sepia_image as si
import numpy as np
import cv2
import os


def test_grey():
    """
        Creates a randomly generated image and checks random pixels of the different
        implementations of greyscale images against the expected values
    """
    randarr = np.random.randint(0,256,size=(100, 200, 3))
    cv2.imwrite("rand.jpeg", randarr)
    image = cv2.imread("rand.jpeg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    grey_python = gi("rand.jpeg", implementation='python')
    grey_numpy = gi("rand.jpeg", implementation='numpy')
    grey_numba = gi("rand.jpeg", implementation='numba')

    rand = [np.random.randint(0, 100), np.random.randint(0, 200)]
    r,g,b = image[rand[0],rand[1],0], image[rand[0],rand[1],1], image[rand[0],rand[1],2]
    sum = r*0.21 + g*0.72 + b*0.07
    pixel = np.empty(3)
    pixel[:] = sum
    pixel = pixel.astype("uint8")
    os.remove("rand.jpeg")

    assert np.all(pixel == grey_python[rand[0], rand[1], :])
    assert np.all(pixel == grey_numpy[rand[0], rand[1], :])
    assert np.all(pixel == grey_numba[rand[0], rand[1], :])



def test_sepia():
    """
        Creates a randomly generated image and checks random pixels of the different
        implementations of sepia images against the expected values
    """
    randarr = np.random.randint(0,256,size=(100, 200, 3))
    cv2.imwrite("rand.jpeg", randarr)
    image = cv2.imread("rand.jpeg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    sepia_python = si("rand.jpeg", implementation='python')
    sepia_numpy = si("rand.jpeg", implementation='numpy')
    sepia_numba = si("rand.jpeg", implementation='numba')

    rand = [np.random.randint(0, 100), np.random.randint(0, 200)]
    sepia_filter = np.array([ [ 0.272, 0.534, 0.131], [ 0.349, 0.686, 0.168], [0.393, 0.769, 0.189] ])

    pixel = np.empty(3)
    pixel = image[rand[0], rand[1]]
    pixel = np.dot(pixel, sepia_filter.T)
    pixel[np.where(pixel>255)] = 255
    pixel = pixel.astype("uint8")
    os.remove("rand.jpeg")

    assert np.all(pixel == sepia_python[rand[0], rand[1], :])
    assert np.all(pixel == sepia_numpy[rand[0], rand[1], :])
    assert np.all(pixel == sepia_numba[rand[0], rand[1], :])
