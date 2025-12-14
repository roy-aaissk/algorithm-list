from __future__ import annotations
import sys
from typing import List, Tuple


def parse_input() -> Tuple[int, int, List[Tuple[int,int]]]:
    tokens = list(map(int, sys.stdin.read().split()))
    if not tokens:
        return 0, 0, []
    it = iter(tokens)
    n = next(it)
    capacity = next(it)
    items = []
    for _ in range(n):
        w = next(it)
        v = next(it)
        items.append((w, v))
    return n, capacity, items


def knapsack_01(n: int, capacity: int, items: List[Tuple[int,int]]) -> int:
    dp = [0] * (capacity + 1)
    for w, v in items:
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[capacity]


def main() -> None:
    n, capacity, items = parse_input()
    res = knapsack_01(n, capacity, items)
    print(res)


if __name__ == "__main__":
    main()
