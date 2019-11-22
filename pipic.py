#!/usr/bin/env python3

from PIL import Image
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("--width")
argparser.add_argument("--height")
argparser.add_argument("--outfile", default="pi.png")
argparser.add_argument("--infile", default="pi.txt")
args = argparser.parse_args()

width = int(args.width)
height = int(args.height)

max_cursor = width * height

img = Image.new('RGB', (width, height))
cursor = 0


def draw_pixel(img, cursor, digit, height):
    y = int(cursor / height)
    x = cursor - y * height
    shade = 25*digit
    img.putpixel((x,y), (shade, shade, shade))


with open(args.infile) as f:
    while cursor < max_cursor:
        char = f.read(1)
        digit = int(char)
        draw_pixel(img, cursor, digit, height)
        cursor += 1

img.save(args.outfile)
