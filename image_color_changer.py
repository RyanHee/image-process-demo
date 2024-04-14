# import
from PIL import Image

# open image
circle_img = Image.open('img/circle.png')

# convert image
circle_img = circle_img.convert('RGBA')

# load pixel data
pixels = circle_img.load()

# iterate through the image to change white pixels to green
for i in range(circle_img.width):
    for j in range(circle_img.height):
        # if current pixel is white, change it to green
        r, g, b, a = pixels[i, j]
        if r > 0:
            # replace with green pixel
            pixels[i, j] = (0, 255, 0, 255)

# save
circle_img.save('img/circle_green.png')

# close
circle_img.close()
