from packagecustom_B.opencv_module_a import ImageArithmetic
from packagecustom_B.opencv_module_b import OpenCVImageProcessor
img_handler_1 = OpenCVImageProcessor()
img_handler_1.read_image('packagecustom_B/imagedata/Test1.jpg')
img_handler_2 = OpenCVImageProcessor()
img_handler_2.read_image('packagecustom_B/imagedata/Test2.jpg')
img_handler_1.resize_image(640,480)
img_handler_2.resize_image(640, 480)

img_arth = ImageArithmetic()
img_handler_1.image = img_arth.add_images(img_handler_1.image, img_handler_2.image)
print(img_handler_1.image.shape)