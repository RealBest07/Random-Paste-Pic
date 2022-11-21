import glob
import random
from PIL import Image


img_bg = Image.open('circle.jpg')
width, height = img_bg.size
images = glob.glob('*.png')
for img in images:
    img = Image.open(img)
    x = random.randint(40, width-40)
    y = random.randint(40, height-40)
    img_bg.paste(img, (x, y, x+10, y+10))
img_bg.save('result.png', 'PNG')
# https://stackoverflow.com/questions/55576760/how-can-i-randomly-add-20-images10x10-in-an-empty-background-image-200x200-i