# import modules that are needed for project
from PIL import Image
import os, shutil

# creating class that inherits from parent class object
class MyImage(object):

	# function that opens image
	def __init__(self, input_path):
		while True:
			# set path variable equal to the path the user inputs
			# the os.path.abspath() function switches forward slashes to backslashes
			self.path = os.path.abspath(input_path)
			try:
				# attempt to open image from the path user gives
				self.img = Image.open(self.path)
				# if attempt is successful no need to loop anymore so break out of while loop
				break
			except:
				# if user gives faulty path have them enter a new one
				print "File not found please try again."
				input_path = raw_input('> ')

	# function switches a pixel from color to gray
	def grey(self, pixel):
		# algorithm for turning pixel to gray
		# casting value into int because that is what putpixel() function takes
		rgb = int( (pixel[0] + pixel[1] + pixel[2]) / 3 )
		return (rgb)

	# function turns the image object that is inialized in __init__ to gray
	def to_grayscale(self):
		# gets size of image
		size = self.img.size
		# create a new blank image the exact size as our original image 
		# I don't exactly know what "L" stands for all I know is it is a mode?
		self.gray_img = Image.new("L", size)
		# for loops to go through each pixel in our image
		for x in range(0, size[0]):
			for y in range(0, size[1]):
				loc = (x, y)
				# retrieves pixel at current location
				pixel = self.img.getpixel(loc)
				# turn the pixel gray then put it into our new img 
				self.gray_img.putpixel(loc, self.grey(pixel))

	# function saves image object to same location it was found in
	def save_grayscale(self):
		try:
			# name the file grey_ plus whatever the name of the original image is
			# which is what the function os.path.basename() does
			filename = "grey_" + os.path.basename(self.path)
			# this saves image to the same location the program is running
			self.gray_img.save(filename)
			# this is location of new image we just saved os.getcwd() gets the folder the program is sitting in
			dir = os.getcwd() + '\\' + filename
			# this is location we would like to move the image to os.path.dirname() gets us the location of the original image
			save_to = os.path.dirname(self.path)
			try:
				# shutil.move() will move our image from its current location (dir) to the location we
				# want to save it to (save_to)
				shutil.move(dir, save_to)
			except:
				# this executes if there is a file with same name in the place we are saving to
				print "There seems to be a " + filename + " already saved in " + save_to + " so I saved it here: " + dir
		except:
			# this executes if the user of the class calls save_grayscale() before turning the image gray
			print "Please call to_grayscale before calling save_grayscale"
