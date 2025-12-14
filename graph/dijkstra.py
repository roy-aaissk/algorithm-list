from __future__ import annotations
import sys
import heapq
from typing import List, Tuple


def parse_input() -> Tuple[int, List[Tuple[int,int,int]], int]:
    tokens = list(map(int, sys.stdin.read().split()))
    if not tokens:
        return 0, [], 0
    it = iter(tokens)
    n = next(it)
    m = next(it)
    edges = []
    for _ in range(m):
        u = next(it)
        v = next(it)
        w = next(it)
        edges.append((u - 1, v - 1, w))
    start = next(it) - 1
    return n, edges, start


def dijkstra(n: int, edges: List[Tuple[int,int,int]], start: int) -> List[float]:
    adj: List[List[Tuple[int,int]]] = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    INF = float('inf')
    dist = [INF] * n
    dist[start] = 0
    h = [(0, start)]
    while h:
        d, u = heapq.heappop(h)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(h, (nd, v))
    return dist


def main() -> None:
    n, edges, start = parse_input()
    if n == 0:
        return
    dist = dijkstra(n, edges, start)
    out = []
    for d in dist:
        out.append("INF" if d == float('inf') else str(d))
    print(" ".join(out))


if __name__ == "__main__":
    main()
