# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 13:15:32 2021

@author: Oscar
"""

from PIL import Image
blank = Image.new(mode = "RGB", size = (1000, 360), color = (255, 255, 255))

def make_square(im):
    print (im.size)
    (width, height) = im.size
    x = int((width/height)*256)
    print (x)
    im = im.resize ((x, 256))
    return im

    
im1 = Image.open ("1.jpg")
im2 = Image.open ("2.jpg")
im3 = Image.open ("3.jpg")
im4 = Image.open ("4.jpg")
im5 = Image.open ("5.jpg")
im6 = Image.open ("6.jpg")

im1 = make_square(im1)
blank.paste(im1, (31, 20))

im2 = make_square(im2)
blank.paste(im2, (190, 60))

im3 = make_square(im3)
blank.paste(im3, (347, 20))

im4 = make_square(im4)
blank.paste(im4, (503, 60))

im5 = make_square(im5)
blank.paste(im5, (661, 20))

im6 = make_square(im6)
blank.paste(im6, (825, 60))

blank.show()