from __future__ import annotations
import sys
from typing import List, Tuple


def parse_input() -> Tuple[str, str]:
    data = sys.stdin.read().splitlines()
    if not data:
        return "", ""
    text = data[0].rstrip('\n')
    pattern = data[1].rstrip('\n') if len(data) > 1 else ""
    return text, pattern


def build_lps(p: str) -> List[int]:
    n = len(p)
    lps = [0] * n
    length = 0
    i = 1
    while i < n:
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text: str, pattern: str) -> int:
    if not pattern:
        return 0
    lps = build_lps(pattern)
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def main() -> None:
    text, pattern = parse_input()
    print(kmp_search(text, pattern))


if __name__ == "__main__":
    main()
