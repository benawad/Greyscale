from PIL import Image
import os, shutil

class MyImage(object):

	def __init__(self, input_path):
		while True:
			self.path = os.path.abspath(input_path)
			try:
				self.img = Image.open(self.path)
				break
			except:
				print "File not found please try again."
				input_path = raw_input('> ')

	def grey(self, pixel):
		gbr = int( (pixel[0] + pixel[1] + pixel[2]) / 3 )
		return (gbr)

	def to_grayscale(self):
		size = self.img.size
		self.gray_img = Image.new("L", size)
		for x in range(0, size[0]):
			for y in range(0, size[1]):
				loc = (x, y)
				pixel = self.img.getpixel(loc)
				self.gray_img.putpixel(loc, self.grey(pixel))

	def save_grayscale(self):
		try:
			filename = "grey_" + os.path.basename(self.path)
			self.gray_img.save(filename)
			dir = os.getcwd() + '\\' + filename
			save_to = os.path.dirname(self.path)
			try:
				shutil.move(dir, save_to)
			except:
				print "Something went wrong when saving :("
		except:
			print "Please call to_grayscale before calling save_grayscale"
