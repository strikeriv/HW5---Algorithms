import sys

def component_graph(n: int, edges: list[tuple[int, int]]) -> tuple[list[int], list[tuple[int, int]]]:
    """
    Compute SCCs and the component graph as described in the problem statement.
    Must run in O(|V| + |E|) time.
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
        
    comp, comp_edges = component_graph(n, edges)
    if not comp:
        print("0 0")
        print()
        return
    
    k = max(comp) + 1
    comp_edges_sorted = sorted(comp_edges)
    p = len(comp_edges_sorted)
    
    print(k, p)
    print(" ".join(str(c) for c in comp))
    for x, y in comp_edges_sorted:
        print(x, y)
        
if __name__ == "__main__":
    solve()