import numpy as np
import os
import re

from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# EDIT HERE
dir_path = 'C:\\Users\\minato\\Desktop\\aaa'
extention = '.png'

# CODES
mask_dir = os.path.join(dir_path, 'mask')
if not os.path.exists(mask_dir):
    os.makedirs(mask_dir)


def make_mask(filename):
    print('  make a file')
    try:
        im = Image.open(filename)
    except:
        print('failed to open an image')
        return 1
    im = im.convert('RGBA')
    image = np.asarray(im)
    height, width, ch = image.shape
    print('  height:'+str(height)+' width:'+str(width))
    newimg = Image.new('RGBA', (width, height))
    white = 0
    black = 0
    for h in range(height):
        for w in range(width):
            alpha = image[h, w][3]
            if alpha <= 100:
                newimg.putpixel((w, h), (0, 0, 0, 255))
                black += 1
            else:
                newimg.putpixel((w, h), (255, 255, 255, 255))
                white += 1
    newimg.save(os.path.join(mask_dir, filename))
    print('  white:'+str(white)+' black:'+str(black))
    print('done')
    print('')
    return 0


targets = os.listdir(dir_path)
os.chdir(dir_path)
skipped_number = 0
file_number = 0
for filename in targets:
    if re.search(extention, filename):
        file_number += 1
        print('filename:'+filename)
        skipped_number += make_mask(filename)

print('RESULTS')
print('     ALL:'+str(file_number))
print('    DONE:'+str(file_number-skipped_number))
print('    SKIP:'+str(skipped_number))
