from os.path import join, dirname
from itertools import product

import cv2 as cv
import numpy as np


def segmentation(filename, k=10):
    img = cv.imread(filename)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    distnaces = compute_distances(
        gray, metric=intensity, neighbours=grid_neighbours)


# def compute_distances(image, metric, neighbours):
#     n, m = image.shape
#     size = n*m
#     distances = np.ones((size, size)) * np.inf
#
#     for i in range(n):
#         for j in range(m):
#             pix1 = j + i*n
#             for x, y in neighbours(i, j, image.shape):
#                 pix2 = j + i*n, x + y*n
#                 if np.isinf(distances[pix1, pix2]):
#                     if np.isinf(distances[pix2, pix1]):
#                     d = metric(image[i, j], image[x, y])
#                     distances[pix1, pix2] = d
#
#     distances[np.diag_indices(size)] = 0
#     return distances


def compute_distances(image):
    n, m = image.shape
    size = n * m
    distances = np.ones((size, size)) * np.inf
    distances[np.diag_indices(size)] = 0

    for i in range(size):
        for j in range(i + 1, size - 1):
            print(i, j)


def intensity(x, y):
    return abs(x - y)


def grid_neighbours(i, j, shape):
    n, m = shape
    deltas = -1, 0, 1
    for dx, dy in product(deltas, deltas):
        if dx == dy == 0:
            continue
        nx, ny = i + dx, j + dy
        if (0 <= nx < n) and (0 <= ny < m):
            yield nx, ny


def main():
    # filename = join(dirname(dirname(__file__)), 'images', 'chimps.jpg')
    # segmentation(filename)
    compute_distances(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


if __name__ == '__main__':
    main()
