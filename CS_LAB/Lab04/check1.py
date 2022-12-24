# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:10:31 2021

@author: Oscar
"""

from PIL import Image
blank = Image.new(mode = "RGB", size = (512, 512), color = (255, 255, 255))


ca = Image.open ("ca.jpg")  
ca = ca.resize ((256, 256))  
blank.paste(ca, (0, 0))

im = Image.open ("im.jpg")   
im = im.resize ((256, 256))  
blank.paste(im, (256, 0))


hk = Image.open ("hk.jpg") 
hk = hk.resize ((256, 256))    
blank.paste(hk, (0, 256))

bw = Image.open ("bw.jpg") 
bw = bw.resize ((256, 256))    
blank.paste(bw, (256, 256))

blank.show()