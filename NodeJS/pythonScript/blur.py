from imageio import imread, imsave
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys

def update_progress(progress):
    print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(progress * 50), progress*100), end="", flush=True)

def average(img, x, y, blurfactor):
    # Each function itself return the each pixel's rgb value.
    # More blur factor is higher quality of blur effect.
    rtotal = gtotal = btotal = 0
    for y2 in range(y - blurfactor, y + blurfactor + 1):
        for x2 in range(x - blurfactor, x + blurfactor + 1):
            r, g, b = (int(img[y2,x2,0]), int(img[y2,x2,1]), int(img[y2,x2,2]))
            (rtotal,gtotal,btotal) = (rtotal+r,gtotal+g,btotal+b)
    (rAverage,gAverage,bAverage) = (rtotal//((blurfactor*2+1)**2)), (gtotal//((blurfactor*2+1)**2)), (btotal//((blurfactor*2+1)**2))
    return (rAverage, gAverage, bAverage)

def blur(blurfactor):
    # Default file name is 'first.jpg'.
    img = imread('cat.jpg')
    width = img.shape[1]
    height = img.shape[0]

    img2 = Image.new("RGB", (width, height), (0,0,0))
    #img2 = img.copy()

    #print(img2[0,0,0])
    #print(type(img))
    #print(type(img2))

    for y in range(blurfactor, height - blurfactor):
        for x in range(blurfactor, width - blurfactor):
            (r,g,b) = (int(img[y,x,0]),int(img[y,x,1]),int(img[y,x,2]))
            r2, g2, b2 = average(img, x, y, blurfactor)
            #img2[y,x,0], img2[y,x,1], img2[y,x,2] = r2,g2,b2
            img2.putpixel((x,y), (r2,g2,b2))
            progress = (y)/(height-blurfactor)
            update_progress(progress)
    update_progress(1)
    img2.save('blur.jpg')
    img2.show()

def main():
    blur(int(sys.argv[1]))

if __name__ == '__main__':
    main()

