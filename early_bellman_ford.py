import sys

def early_bellman_ford(
n: int,
edges: list[tuple[int, int, int]],
s: int
) -> list[float]:
    """
    Implement the early-stopping Bellman-Ford algorithm.
    Use float("inf") for unreachable vertices.
    Must run in O(n * m) in the worst case, and terminate early when
    a pass performs no updates.
    """
    raise NotImplementedError

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    s = int(next(it))
    
    edges: list[tuple[int, int, int]] = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    dist = early_bellman_ford(n, edges, s)
    out_tokens: list[str] = []
    for d in dist:
        if d == float("inf"):
            out_tokens.append("INF")
        else:
            out_tokens.append(str(int(d)))
        
    print(" ".join(out_tokens))

if __name__ == "__main__":
    solve()