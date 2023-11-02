import cv2
import numpy as np

class ImageArithmetic:
    def __init__(self):
        self.version = (cv2.__version__, np.__version__)
        self.print_version()
    
    def print_version(self):
        print("opencv version: {}".format(self.version[0]))
        print("python version: {}".format(self.version[1]))

    def add_images(self, image1, image2):
        return cv2.add(image1, image2)

    def subtract_images(self, image1, image2):
        return cv2.subtract(image1, image2)

    def multiply_image(self, image1, alpha):
        return cv2.multiply(image1, alpha)

    def divide_image(self, image1, beta):
        return cv2.divide(image1, beta)

    def blend_images(self, image1, image2, alpha, beta, gamma):
        return cv2.addWeighted(image1, alpha, image2, beta, gamma)

    def save_image(self, file_path, image):
        cv2.imwrite(file_path, image)
