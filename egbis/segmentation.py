from os.path import join, dirname

import cv2 as cv


def segmentation(filename, k=10):
    img = cv.imread(filename)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    print(gray.shape)


def main():
    filename = join(dirname(dirname(__file__)), 'images', 'chimps.jpg')
    segmentation(filename)


if __name__ == '__main__':
    main()
