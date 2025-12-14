from __future__ import annotations
import sys
import bisect
from typing import List


def parse_input() -> List[int]:
    tokens = list(map(int, sys.stdin.read().split()))
    if not tokens:
        return []
    n = tokens[0]
    return tokens[1:1 + n]


def lis_length(arr: List[int]) -> int:
    # patience sorting O(n log n)
    piles: List[int] = []
    for x in arr:
        i = bisect.bisect_left(piles, x)
        if i == len(piles):
            piles.append(x)
        else:
            piles[i] = x
    return len(piles)


def main() -> None:
    arr = parse_input()
    print(lis_length(arr))


if __name__ == "__main__":
    main()
