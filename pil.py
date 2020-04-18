from PIL import Image
import PIL.ImageOps
import os
directory = "In"
outdirectory = "Out"
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
       
        
        infile = (os.path.join(directory, filename))
        outfile = (os.path.join(outdirectory, "OUT_" + filename))
        print "Doing... " + infile + " to " + outfile
        image = Image.open(infile)
        inverted_image = PIL.ImageOps.invert(image)
        inverted_image.save(outfile)
        continue
    else:
        continue
