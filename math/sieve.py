from __future__ import annotations
import sys
from typing import List


def parse_input() -> int:
    data = sys.stdin.read().strip()
    if not data:
        return 0
    return int(data.split()[0])


def sieve_primes(n: int) -> List[int]:
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for k in range(p * p, n + 1, p):
                is_prime[k] = False
        p += 1
    return [i for i, val in enumerate(is_prime) if val]


def main() -> None:
    n = parse_input()
    primes = sieve_primes(n)
    print(" ".join(map(str, primes)))


if __name__ == "__main__":
    main()
