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


def lower_bound(arr: List[int], target: int) -> int:
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    if lo < len(arr):
        return lo
    return -1


def main() -> None:
    arr, target = parse_input()
    print(lower_bound(arr, target))


if __name__ == "__main__":
    main()
