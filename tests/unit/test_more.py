import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from sort.merge_sort import merge_sort
from sort.heap_sort import heap_sort
from search.lower_bound import lower_bound
from graph.bfs import bfs
from number.sieve import sieve_primes
from dp.lis import lis_length


def test_merge_sort():
    assert merge_sort([5, 3, 8, 1, 2, 7]) == [1, 2, 3, 5, 7, 8]


def test_heap_sort():
    assert heap_sort([5, 3, 8, 1, 2, 7]) == [1, 2, 3, 5, 7, 8]


def test_lower_bound():
    assert lower_bound([1, 3, 4, 7, 9], 5) == 3


def test_bfs():
    n = 4
    adj = [[1], [0, 2], [1, 3], [2]]
    assert bfs(n, adj, 0) == [0, 1, 2, 3]


def test_sieve():
    assert sieve_primes(10) == [2, 3, 5, 7]


def test_lis():
    assert lis_length([3, 1, 2, 1, 8, 5]) == 3
