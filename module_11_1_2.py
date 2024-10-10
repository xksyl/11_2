from PIL import Image

image = Image.open('bar 2.png')

reaized = image.resize((200, 200))
reaized.save('reaized.png')


color = image.convert('L')
color.save('color.png')


