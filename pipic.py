#!/usr/bin/env python3
from random import Random

from PIL import Image
import argparse


class RandomInput:

    def __init__(self):
        self.generator = Random()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def read(self, _):
        return int(self.generator.random() * 10 + 0.5)


def draw_pixel(img, cursor, digit, height):
    y = int(cursor / height)
    x = cursor - y * height
    shade = 25*digit
    img.putpixel((x,y), (shade, shade, shade))


def input_stream(random=False, filename=None):
    if random:
        return RandomInput()
    return open(filename)


if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--width")
    arg_parser.add_argument("--height")
    arg_parser.add_argument("--outfile", default="pi.png")
    arg_parser.add_argument("--infile", default="pi.txt")
    arg_parser.add_argument("--random", action="store_true")
    arg_parser.add_argument("--filter", default="0123456789")
    arg_parser.add_argument("--skip_color", default="0")
    args = arg_parser.parse_args()

    width = int(args.width)
    height = int(args.height)

    max_cursor = width * height

    img = Image.new('RGB', (width, height))
    cursor = 0

    with input_stream(filename=args.infile, random=args.random) as f:
        while cursor < max_cursor:
            char = f.read(1)
            if not char in args.filter:
                char = args.skip_color
            digit = int(char)
            draw_pixel(img, cursor, digit, height)
            cursor += 1

    img.save(args.outfile)
