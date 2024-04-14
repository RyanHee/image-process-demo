from PIL import Image

square_image = Image.open('img/square_bg.png')
circle_image = Image.open('img/circle_bg.png').convert('RGBA')

# resize square image
square_image = square_image.resize((circle_image.width, circle_image.height))

# put square on the middle circle image
circle_image.paste(square_image, (0, 0), square_image)

# save image
circle_image.save('img/circle+square.png')

# close images
circle_image.close()
square_image.close()
