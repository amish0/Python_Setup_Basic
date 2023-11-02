import os
import cv2
import numpy as np

class OpenCVImageProcessor:
    def __init__(self):
        self.version = (cv2.__version__, np.__version__)
        self.image = None
        self.print_version()
    
    def print_version(self):
        print("opencv version: {}".format(self.version[0]))
        print("python version: {}".format(self.version[1]))
    
    def read_image(self, file_name = None):
        if file_name is not None:
            self.image = cv2.imread(file_name)

    def show_image(self):
        cv2.imshow('Image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_image(self, output_file_path):
        cv2.imwrite(output_file_path, self.image)

    def convert_to_grayscale(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def resize_image(self, width, height):
        self.image = cv2.resize(self.image, (width, height))

    def draw_rectangle(self, x, y, width, height):
        cv2.rectangle(self.image, (x, y), (x + width, y + height), (0, 255, 0), thickness=2)

    def draw_circle(self, cx, cy, radius):
        cv2.circle(self.image, (cx, cy), radius, (0, 0, 255), thickness=2)

    def draw_line(self, x1, y1, x2, y2):
        cv2.line(self.image, (x1, y1), (x2, y2), (255, 0, 0), thickness=2)

    def apply_gaussian_blur(self):
        self.image = cv2.GaussianBlur(self.image, (5, 5), 0)

    def detect_edges(self, threshold1, threshold2):
        self.image = cv2.Canny(self.image, threshold1, threshold2)

    def find_and_draw_contours(self):
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, 30, 100)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(self.image, contours, -1, (0, 255, 0), 2)

if __name__ == "__main__":
    # Example usage:
    image_processor = OpenCVImageProcessor('image.jpg')
    image_processor.convert_to_grayscale()
    image_processor.resize_image(200, 200)
    image_processor.draw_rectangle(50, 50, 100, 100)
    image_processor.show_image()
    image_processor.save_image('output.jpg')

