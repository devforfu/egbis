import pytest
import numpy as np

from egbis.segmentation import grid_neighbours
from egbis.segmentation import compute_distances, intensity, grid_neighbours


def test_grid_neighbours_returns_valid_neighbours_only():
    expected = np.array([
        [3, 5, 5, 5, 3],
        [5, 8, 8, 8, 5],
        [5, 8, 8, 8, 5],
        [3, 5, 5, 5, 3]
    ])
    n, m = shape = expected.shape

    actual = np.array([
        len(list(grid_neighbours(i, j, shape)))
        for i in range(n) for j in range(m)])

    assert len(actual) == n * m
    assert np.array_equal(expected.flatten(), actual)


def test_grid_neighbours_distance_computation_returns_valid_distances_matrix():
    image = np.array([
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 4]
    ])

    distances = compute_distances(
        image=image,
        metric=intensity,
        neighbours=grid_neighbours)

    assert square_matrix(distances)
    assert zeros_on_diagonal(distances)
    assert symmetric_matrix(distances)


def square_matrix(matrix):
    return matrix.shape[0] == matrix.shape[1]


def zeros_on_diagonal(matrix):
    return np.diag(matrix).sum() == 0


def symmetric_matrix(matrix, tol=1e-8):
    return np.allclose(matrix, matrix.T, atol=tol)

