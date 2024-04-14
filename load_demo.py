# import
from PIL import Image

# open image
image = Image.open('image.png')

# load pixel data
pixels = image.load()

# access pixel at coordinates (x, y) ((0, 0) is top left)

pixel = pixels[x,y]

print(pixel)

# close image
image.close()