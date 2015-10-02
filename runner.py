# this file is very basic all it does is use the MyImage class
from Greyscale import MyImage

print "Enter absolute path to file (case sensitive)"
path = raw_input('$ ')

# instantiates MyImage object
test = MyImage.MyImage(path)

# turns image gray
test.to_grayscale()

# saves image
test.save_grayscale()

# this is here so when you run the .exe file the command prompt does not 
# open and close instantly and you can't see anything that happens
raw_input('All done! (press enter to end script)')
