from __future__ import annotations
import sys
from typing import List, Tuple


def parse_input() -> List[int]:
    tokens = list(map(int, sys.stdin.read().split()))
    if not tokens:
        return []
    n = tokens[0]
    arr = tokens[1:1 + n]
    return arr


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


def main() -> None:
    arr = parse_input()
    sorted_arr = quick_sort(arr)
    print(" ".join(map(str, sorted_arr)))


if __name__ == "__main__":
    main()
