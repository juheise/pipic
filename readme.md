# PiPic

Creates a visual representation of Pi's decimal places. Supports 1M decimals right out of the box.

## Installing

Requires Python 3 and pipenv installed. Developed for Linux, but may run on any system that runs Python 3.

```commandLine
pip install pipenv
pipenv install # this line required only for the first time
```

## Usage

```commandLine
pipenv run ./pipic.py --width 1000 --height 1000
```

### Available Arguments

- width: picture width in pixels
- height: picture height in pixels
- infile (optional): file to read decimal places from; expects text; can only deal with integers, other symbols will cause errors
- outfile (optional): file
- random (optional): set this flag to use random input instead
- filter (optional): defines which decimal values will be accepted; accepts a string like `314`, which will accept all
  digits `3`, `1` and `4`. Default is `0123456789`
- skip_color (optional): define the color to use, when a pixel is skipped due to being filtered out; accepts 0-9, default is zero


### How to create pictures larger than 1000x1000

PiPic only supports 1M decimal places of Pi right out the box. If you want more you must supply your own data. Put all
the decimals in a text file (but without the leading `3.` - only the decimals) and supply the text file via the
`--infile /my/file.txt` command line argument.
