 #! python3
   # resizeAndAddLogo.py - Resizes all images in current working directory to fit
   # in a 300x300 square, and adds catlogo.png to the lower-right corner.
import os
from PIL import Image

SQUARE_FIT_SIZE_WIDTH = 1080
SQUARE_FIT_SIZE_HEIGHT = 1340
LOGO_FILENAME = 'watermark.png'

logoIm = Image.open(LOGO_FILENAME)
#logoIm=logoIm.resize((SQUARE_FIT_SIZE_WIDTH,SQUARE_FIT_SIZE_HEIGHT))
logoWidth, logoHeight = logoIm.size

# TODO: Loop over all files in the working directory.
os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
   if not (filename.endswith('.png') or filename.endswith('.jpg')) \
       or filename == LOGO_FILENAME:
      continue # skip non-image files and the logo file itself

   im = Image.open(filename)
   width, height = im.size

   if width > SQUARE_FIT_SIZE_WIDTH and height > SQUARE_FIT_SIZE_HEIGHT or width < SQUARE_FIT_SIZE_WIDTH and height < SQUARE_FIT_SIZE_HEIGHT :
       # Calculate the new width and height to resize to.
      # if width > height:
      #    height = int((SQUARE_FIT_SIZE / width) * height)
      #    width = SQUARE_FIT_SIZE
      # else:
      #    width = int((SQUARE_FIT_SIZE / height) * width)
      #    height = SQUARE_FIT_SIZE

       # Resize the image.
      print('Resizing %s...' % (filename))
      im = im.resize((SQUARE_FIT_SIZE_WIDTH, SQUARE_FIT_SIZE_HEIGHT))


# TODO: Check if image needs to be resized.

# TODO: Calculate the new width and height to resize to.

# TODO: Resize the image.

# TODO: Add the logo.
   print('Adding logo to %s...' % (filename))
   im.paste(logoIm, (SQUARE_FIT_SIZE_WIDTH - logoWidth, SQUARE_FIT_SIZE_HEIGHT - logoHeight), logoIm)

 # Save changes.
   im.save(os.path.join('withLogo', filename))

   # TODO: Save changes.