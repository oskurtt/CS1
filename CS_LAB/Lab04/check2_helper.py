# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:46:27 2021

@author: Oscar
"""
from PIL import Image
blank = Image.new(mode = "RGB", size = (512, 512), color = (255, 255, 255))

def make_square(im):
    print (im.size)
    (width, height) = im.size
    x = min(width, height)
    im = im.crop ((0, 0, x, x))
    im = im.resize ((256, 256))
    return im

    
ca = Image.open ("ca.jpg")
im = Image.open ("im.jpg")
hk = Image.open ("hk.jpg")
bw = Image.open ("bw.jpg")

ca = make_square(ca)
blank.paste(ca, (0, 0))

im = make_square(im)
blank.paste(im, (256, 0))

hk = make_square(hk)
blank.paste(hk, (0, 256))

bw = make_square(bw)
blank.paste(bw, (256, 256))

blank.show()