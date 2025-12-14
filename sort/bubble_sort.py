from __future__ import annotations
import sys
from typing import List


def parse_input() -> List[int]:
    tokens = list(map(int, sys.stdin.read().split()))
    if not tokens:
        return []
    n = tokens[0]
    return tokens[1:1 + n]


def bubble_sort(arr: List[int]) -> List[int]:
    a = arr[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def main() -> None:
    arr = parse_input()
    print(" ".join(map(str, bubble_sort(arr))))


if __name__ == "__main__":
    main()
