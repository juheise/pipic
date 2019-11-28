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


def buffer_to_image(buffer, width):
    max_shade = 0
    for b in buffer:
        max_shade = max(b, max_shade)
    height = int(len(buffer) / width) +1
    img = new_image(width, height)
    x = 0
    y = 0
    for b in buffer:
        if x == width:
            x = 0
            y += 1
        shade = int(b/max_shade * 255)
        img.putpixel((x,y), (shade, shade, shade))
        x += 1
    return img
