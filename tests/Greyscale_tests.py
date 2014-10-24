from nose.tools import *
from Greyscale import MyImage
from PIL import Image
import Greyscale

# tests to see if MyImage object instantiates correctly
# this will only work on my computer because you don't the same 
# file path on your computer
# so if you want to test this change the parameter for MyImage()
def test_image():
	new_img = MyImage.MyImage("C:/Users/Ben/Tulips.jpg")
	assert_equal(new_img.path, "C:\\Users\\Ben\\Tulips.jpg")
	assert_equal(new_img.img, Image.open(new_img.path))

# tests whether my algorithm works for turning a pixel from
# color to gray works
# same as above change MyImage() parameter
def test_grey():
	new_img = MyImage.MyImage("C:/Users/Ben/Tulips.jpg")
	pixel = [365, 365, 365]
	gbr_value = new_img.grey(pixel)
	assert_equal(gbr_value, 365)
