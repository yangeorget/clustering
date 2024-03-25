from typing import Sequence

import numpy as np
from numpy.typing import NDArray

from clustering_algorithms.clustering_algorithm import ClusteringAlgorithm


class CMeans(ClusteringAlgorithm):
    """
    A Numpy implementation of the C-Means clustering_algorithms algorithm.
    """

    def __init__(self, k: int, iterations: int, m: int = 2):
        """
        :param k: the number of clusters
        :param iterations: the number of iterations
        :param m: the fuzzifier factor (should be > 1, default to 2)
        """
        super().__init__(k, iterations)
        self.m = m

    def compute_centroids(self, points: NDArray, weights: NDArray) -> NDArray:
        """
        Computes the centroids given the weights.
        :param points: a nxd matrix
        :param weights: a nxk matrix
        :return: a kxd matrix where k is the number of clusters and d the number of dimensions
        """
        wm = weights**self.m
        return (points.T @ wm / np.sum(wm, axis=0)).T

    def fit(self, points: NDArray) -> Sequence[NDArray]:
        n = points.shape[0]
        weights = np.array(np.random.dirichlet(np.ones(self.k), n))
        centroids = self.compute_centroids(points, weights)
        for iteration in range(self.iterations):
            clusters = np.argmax(weights, axis=1)
            self.log_iteration(iteration, centroids, clusters)
            weights = self.predict(points, centroids)
            new_centroids = self.compute_centroids(points, weights)
            if np.all(new_centroids == centroids):  # type: ignore
                break
            centroids = new_centroids
        return centroids, clusters, weights

    def predict(self, points: NDArray, centroids: NDArray) -> NDArray:
        nn_weights = self.distances(points, centroids) ** (-2 / (self.m - 1))
        return nn_weights / np.sum(nn_weights, axis=1, keepdims=True)
