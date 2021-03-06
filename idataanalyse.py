#!/usr/bin/python3

#This is the cli version of the iDataAnalyse app

import json
from PIL import Image
from pprint import pprint

def calculate_values_required():
    pass

# Replace the <filename> with the image file

def img_to_raw(img):
    im = Image.open(img)
    px = im.load()
    dct = dict()
    vertical_low = 0
    vertical_high = 450
    horizontal_low = 0
    horizontal_high = 900
    width, height = im.size
    vertical_pixel_increment = (vertical_high - vertical_low) / height
    print(vertical_pixel_increment)
    horizontal_pixel_increment = (horizontal_high - horizontal_low) / width
    base_h = horizontal_low
    cperrow = 4
    for a in range(1, width):
        found = list()
        base = vertical_low
        lst = list()
        for x in range(0, cperrow):
            for b in range(1, height+1):
                if px[a, b] not in found and px[a, b] != (0,0,0):
                    found.append(px[a,b])
                    lst.append(base)
                    break
                base = base + vertical_pixel_increment
        ttb = vertical_high
        dct[base_h] = lst
        base_h = base_h + horizontal_pixel_increment
    return dct

def push_to_values():
    pass

if __name__ == "__main__":
    pxls = img_to_raw(<filename>)
    pprint(pxls)
