from nose.tools import *
from Greyscale import MyImage
from PIL import Image
import Greyscale

def test_image():
	new_img = MyImage.MyImage("C:/Users/Ben/Tulips.jpg")
	assert_equal(new_img.path, "C:\\Users\\Ben\\Tulips.jpg")
	assert_equal(new_img.img, Image.open(new_img.path))

def test_grey():
	new_img = MyImage.MyImage("C:/Users/Ben/Tulips.jpg")
	pixel = [365, 365, 365]
	gbr_value = new_img.grey(pixel)
	assert_equal(gbr_value, 365)
