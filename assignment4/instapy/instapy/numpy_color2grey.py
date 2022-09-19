import cv2



def greyscale_filter(filename):
    """
        Greyscale filter for images, implemented with numpy
        Args:
            filename (string): filename of image to be filteres
        Returns:
            writes an imagefile in format <original_filename>_greyscale.jpeg
    """
    image = cv2.imread(filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    r,g,b = image[:,:,0], image[:,:,1], image[:,:,2]
    sum = r*0.21 + g*0.72 + b*0.07
    image[:,:,0] = image[:,:,1] = image[:,:,2] = sum

    image = image.astype("uint8")
    temp = filename.split(".")
    new_filename = temp[0] + "_greyscale.jpeg"
    cv2.imwrite(new_filename, image)

greyscale_filter("rain.jpeg")
