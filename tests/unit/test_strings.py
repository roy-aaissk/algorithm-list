import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from strings.kmp import kmp_search


def test_kmp():
    assert kmp_search('abxabcabcaby', 'abcaby') == 6
