from Greyscale import MyImage

print "Enter absolute path to file (case sensitive)"
path = raw_input('> ')

test = MyImage.MyImage(path)
test.to_grayscale()
test.save_grayscale()
raw_input('All done! (press enter to end script)')
