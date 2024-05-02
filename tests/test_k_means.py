import numpy as np

from clustering_algorithms.k_means import KMeans


class TestKMeans:
    def test_compute_centroids_1_1(self) -> None:
        centroids = KMeans(1).compute_centroids(np.array([[1, 2]]), np.array([0]))
        assert np.all(centroids == np.array([[1, 2]]))

    def test_compute_centroids_1_2(self) -> None:
        centroids = KMeans(1).compute_centroids(np.array([[1, 3], [5, 3]]), np.array([0, 0]))
        assert np.all(centroids == np.array([[3, 3]]))

    def test_compute_centroids_2_2(self) -> None:
        centroids = KMeans(2).compute_centroids(np.array([[1, 3], [5, 3]]), np.array([0, 1]))
        assert np.all(centroids == np.array([[1, 3], [5, 3]]))

    def test_fit_1(self) -> None:
        centroids, clusters = KMeans(1, 2).fit(np.array([[1, 3], [5, 3]]))
        assert np.all(centroids == np.array([[3, 3]]))
        assert np.all(clusters == np.array([0, 0]))

    def test_fit_2(self) -> None:
        centroids, clusters = KMeans(2, 1).fit(np.array([[1, 3], [5, 3]]))
        assert np.all(np.sort(centroids, axis=0) == np.array([[1, 3], [5, 3]]))
        assert np.all(np.sort(clusters, axis=0) == np.array([0, 1]))

    def test_predict(self) -> None:
        clusters = KMeans(1).predict(np.array([[1, 3], [5, 3]]), np.array([3, 3]))
        assert np.all(clusters == np.array([[0, 0]]))