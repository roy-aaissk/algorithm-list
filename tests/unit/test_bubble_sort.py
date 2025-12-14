import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from sort.bubble_sort import bubble_sort


def test_bubble_sort():
    assert bubble_sort([5, 3, 8, 1, 2, 7]) == [1, 2, 3, 5, 7, 8]
