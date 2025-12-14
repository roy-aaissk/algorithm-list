import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from sort.quick_sort import quick_sort


def test_quick_sort():
    assert quick_sort([5, 3, 8, 1, 2, 7]) == [1, 2, 3, 5, 7, 8]
