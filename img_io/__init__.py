from PIL import Image

def draw_pixel(img, cursor, digit, height):
    y = int(cursor / height)
    x = cursor - y * height
    shade = 25*digit
    img.putpixel((x,y), (shade, shade, shade))


def new_image(width, height):
    return Image.new('RGB', (width, height))


def save_image(img, path):
    img.save(path)
