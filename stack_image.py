from PIL import Image

square_image = Image.open('img/square_bg.png')
circle_image = Image.open('img/circle.png').convert('RGBA')
img = Image.open('img/B.png').convert('RGBA')
print(img.mode)
print(square_image.mode)

square_image=square_image.resize((400, 400))
circle_image.paste(img, (200, 200))

#square_image.paste(circle_image, (200, 200), circle_image)
#square_image.save('img/circle+square.png')
circle_image.save('img/circle+square.png')

'''
square_image = square_image.resize((100, 100))
circle_image = circle_image.resize((50, 50))

square_image.paste(circle_image, (25, 25))

square_image.save('img/circle+square.png')
'''
circle_image.close()
square_image.close()
