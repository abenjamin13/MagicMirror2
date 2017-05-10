from PIL import Image, ImageChops
point_table = ([0] + ([255] * 255))

def black_or_b(a, b):
    diff = ImageChops.difference(a, b)
    diff = diff.convert('L')
    # diff = diff.point(point_table)
    h,w=diff.size
    new = diff.convert('RGB')
    new.paste(b, mask=diff)
    return new

a = Image.open('withoutbanana.jpg')
b = Image.open('withbanana.jpg')
c = black_or_b(a, b)
c.save('diff.png')
