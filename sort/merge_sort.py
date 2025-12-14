from __future__ import annotations
import sys
from typing import List


def parse_input() -> List[int]:
    tokens = list(map(int, sys.stdin.read().split()))
    if not tokens:
        return []
    n = tokens[0]
    return tokens[1:1 + n]


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    i = j = 0
    merged: List[int] = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def main() -> None:
    arr = parse_input()
    print(" ".join(map(str, merge_sort(arr))))


if __name__ == "__main__":
    main()
