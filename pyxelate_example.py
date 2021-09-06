from skimage import io
from pyxelate import Pyx, Pal
from sys import argv

img = io.imread(argv[1])
# generate pixel art that is 1/n the size
height, width, _ = img.shape

p = Pyx(factor=2, palette=Pal.MONO_PHOSPHOR_GREEN3, dither='bayer')
p.fit(img)
img_small = p.transform(img) # convert an image with these settings

io.imsave('out/test4.png', img_small)
