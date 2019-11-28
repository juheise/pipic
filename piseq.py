#!/usr/bin/env python3

import argparse
from img_io import save_image, buffer_to_image
from input import select_input_stream

if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--chain")
    arg_parser.add_argument("--outfile", default="pi.png")
    arg_parser.add_argument("--infile", default="pi.txt")
    arg_parser.add_argument("--random", action="store_true")
    arg_parser.add_argument("--find", default="3141592")
    arg_parser.add_argument("--skip_color", default="255")
    arg_parser.add_argument("--match_color", default="0")
    arg_parser.add_argument("--line_width")
    args = arg_parser.parse_args()

    # constants
    max_cursor = int(args.chain)
    stop = len(args.find) - 1

    # variables
    cursor = 0
    index = 0
    buffer = []
    distance = 0

    with select_input_stream(filename=args.infile, random=args.random) as f:
        while cursor < max_cursor:
            char = f.read(1)
            if char == args.find[index]:
                index += 1
            if index == stop:
                buffer.append(distance)
                index = 0
                distance = 0
            cursor += 1
            distance += 1

    img = buffer_to_image(buffer, int(args.line_width))
    save_image(img, args.outfile)
