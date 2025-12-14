from __future__ import annotations
import sys
import heapq
from typing import List


def parse_input() -> List[int]:
    tokens = list(map(int, sys.stdin.read().split()))
    if not tokens:
        return []
    n = tokens[0]
    return tokens[1:1 + n]


def heap_sort(arr: List[int]) -> List[int]:
    h = arr[:]
    heapq.heapify(h)
    res: List[int] = []
    while h:
        res.append(heapq.heappop(h))
    return res


def main() -> None:
    arr = parse_input()
    print(" ".join(map(str, heap_sort(arr))))


if __name__ == "__main__":
    main()
