from __future__ import annotations
import sys
from typing import List, Tuple


def parse_input() -> Tuple[List[int], int]:
    tokens = list(map(int, sys.stdin.read().split()))
    if not tokens:
        return [], -1
    n = tokens[0]
    arr = tokens[1:1 + n]
    target = tokens[1 + n] if len(tokens) > 1 + n else -1
    return arr, target


def binary_search(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def main() -> None:
    arr, target = parse_input()
    print(binary_search(arr, target))


if __name__ == "__main__":
    main()
