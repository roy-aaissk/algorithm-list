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


def linear_search(arr: List[int], target: int) -> int:
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


def main() -> None:
    arr, target = parse_input()
    res = linear_search(arr, target)
    print(res)


if __name__ == "__main__":
    main()
