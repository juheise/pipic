# PiPic

Creates a visual representation of Pi's decimal places

## Installing

```commandLine
pip install pipenv
pipenv install # this line required only for the first time
```

## Usage

Requires Python 3 and pipenv

```commandLine
pipenv run ./pipic.py --width 1000 --height 1000
```

## Available Arguments

- width: picture width in pixels
- height: picture height in pixels
- infile (optional): file to read decimal places from; expects text; can only deal with integers, other symbols will cause errors
- outfile (optional): file
