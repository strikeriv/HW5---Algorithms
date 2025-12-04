import sys

def connected_components(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    """
    n: number of vertices labeled 0..n-1.
    edges: list of undirected edges (u, v).
    Returns a list of components, where each component is a list of vertices.
    Each component list must be sorted in increasing order.
    The list of components must be sorted by each component’s smallest vertex.
    """
    raise NotImplementedError

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    edges: list[tuple[int, int]] = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        
    comps = connected_components(n, edges)
    print(len(comps))
    
    for comp in comps:
        print(" ".join(str(v) for v in comp))
    
if __name__ == "__main__":
    solve()