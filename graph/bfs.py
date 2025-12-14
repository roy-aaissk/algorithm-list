from __future__ import annotations
import sys
from collections import deque
from typing import List, Tuple


def parse_input() -> Tuple[int, List[List[int]], int]:
    tokens = list(map(int, sys.stdin.read().split()))
    if not tokens:
        return 0, [], 0
    it = iter(tokens)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
        adj[v].append(u)
    start = next(it) - 1
    return n, adj, start


def bfs(n: int, adj: List[List[int]], start: int) -> List[int]:
    dist = [-1] * n
    q = deque([start])
    dist[start] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def main() -> None:
    n, adj, start = parse_input()
    if n == 0:
        return
    dist = bfs(n, adj, start)
    print(" ".join(map(str, dist)))


if __name__ == "__main__":
    main()
