import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from dp.knapsack_01 import knapsack_01


def test_knapsack():
    assert knapsack_01(3, 50, [(10, 60), (20, 100), (30, 120)]) == 220
