import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from search.linear import linear_search
from search.binary import binary_search


def test_linear_search():
    assert linear_search([1, 3, 4, 7, 9], 4) == 2


def test_binary_search():
    assert binary_search([1, 3, 4, 7, 9], 4) == 2
