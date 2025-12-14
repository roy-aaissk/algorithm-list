import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from graph.dijkstra import dijkstra


def test_dijkstra():
    n = 4
    edges = [(0, 1, 1), (1, 2, 2), (0, 2, 5), (2, 3, 1)]
    dist = dijkstra(n, edges, 0)
    assert [int(x) for x in dist] == [0, 1, 3, 4]
