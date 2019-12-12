import os
import random
from PIL import Image
from PIL import ImageFile
import argparse
ImageFile.LOAD_TRUNCATED_IMAGES = True

# EDIT HERE
dir_path = './'
extention = '.png'

# CODES


def generate_image(args):
    block = args.block
    multiple = args.scale
    little_w = little_h = block
    width = height = block*multiple
    little = [[0] * little_w for i in range(little_h)]
    for i in range(little_h):
        for j in range(int(little_w/2)):
            little[i][j] = little[i][little_w-j-1] = random.getrandbits(1)

    for i in range(little_h):
        for j in range(little_w):
            if little[i][j]:
                print("□ ", end="")
            else:
                print("■ ", end="")
        print("")
    yn = input("Is this ok? (y/n/x)")
    if yn != "y" and yn != "x":
        generate_image(args)
    elif yn == "x":
        exit()
    else:
        new_img = Image.new('RGBA', (width, height))
        # foreground color
        r = random.randint(0, 255)
        b = random.randint(0, 255)
        g = random.randint(0, 255)
        rgb = (r, g, b, 255)
        # background color
        brgb = (255, 255, 255, 255)
        if args.transparent:
            brgb = (0, 0, 0, 0)

        for h in range(height):
            for w in range(width):
                if little[(h//multiple)][(w//multiple)]:
                    new_img.putpixel((w, h), rgb)
                else:
                    new_img.putpixel((w, h), brgb)
        new_img.save(os.path.join(dir_path, args.output))


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--block", default=12,
                        help="The number of color blocks")
    parser.add_argument("-s", "--scale", default=12,
                        help="Scale of the color blocks; -b 10 -s 5 -> 50x50px")
    parser.add_argument("-o", "--output", default="icon.png",
                        help="The name of output file; icon.png")
    parser.add_argument("-t", "--transparent", default=False, action='store_true',
                        help="Enable the background color transparent")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    generate_image(args)
