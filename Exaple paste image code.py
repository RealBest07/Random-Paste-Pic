from PIL import Image, ImageDraw, ImageFilter
import random

im1 = Image.open('D:\Project\img\\raw\\for dicut\\bg\\32261_jpg.rf.25e3c9094fba4eab03bc92beb5599d29.jpg')
im2 = Image.open('D:\Project\img\\raw\\for dicut\\peanut\\4.png')
minim1x = 0
minim1y = 0
minim2x = 0
minim2y = 0
maxim1x = im1.size[0]
maxim1y = im1.size[1]
maxim2x = im2.size[0]
maxim2y = im2.size[1]
ranpo1x = random.randrange(minim1x,maxim1x)
ranpo1y = random.randrange(minim1y,maxim1y)
# mask_im = Image.open('D:\Project\img\\raw\\for dicut\\peanut\\4.png').convert('L')
print(im2.size[0])
im1.paste(im2,(ranpo1x, ranpo1y), im2) #im2 paste im im1
im1.save('D:/Project/img/rocket_pillow_paste.jpg', quality=100)