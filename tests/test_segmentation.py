import pytest
import numpy as np

from egbis.segmentation import grid_intensity_distances


def test_grid_neighbours_distance_computation_returns_valid_distances_matrix():
    image = np.array([
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 4]
    ])

    distances = grid_intensity_distances(image)

    assert square_matrix(distances)
    assert zeros_on_diagonal(distances)
    assert symmetric_matrix(distances)


def square_matrix(matrix):
    return matrix.shape[0] == matrix.shape[1]


def zeros_on_diagonal(matrix):
    return np.diag(matrix).sum() == 0


def symmetric_matrix(matrix, tol=1e-8):
    return np.allclose(matrix, matrix.T, atol=tol)

