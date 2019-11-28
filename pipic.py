#!/usr/bin/env python3

import argparse
from img_io import draw_pixel, new_image, save_image
from input import select_input_stream

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
    img = new_image(width, height)
    cursor = 0

    with select_input_stream(filename=args.infile, random=args.random) as f:
        while cursor < max_cursor:
            char = f.read(1)
            if not char in args.filter:
                char = args.skip_color
            digit = int(char)
            draw_pixel(img, cursor, digit, height)
            cursor += 1

    save_image(img, args.outfile)
