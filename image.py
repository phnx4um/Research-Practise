import numpy
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys

def main(argv):
    if len(argv) != 2:
        print("Usage: python image.py imagename.png")
        sys.exit (1)

    img=mpimg.imread('images/' + argv[1])
    print(img)

    imgplot = plt.imshow(img)
    plt.show()

if __name__ == "__main__":
    main(sys.argv)
