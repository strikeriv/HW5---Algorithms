import sys

def update_mst(
n: int,
edges: list[tuple[int, int, int]],
mst_edge_indices: list[int],
new_edge: tuple[int, int, int],
) -> list[int]:
    """
    Update the MST after inserting ’new_edge’, as described in the problem statement.
    Must run in O(n + m) time.
    """
    raise NotImplementedError

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    edges: list[tuple[int, int, int]] = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
        
    mst_edge_indices: list[int] = []
    for _ in range(n - 1):
        mst_edge_indices.append(int(next(it)))
        
    u_new = int(next(it))
    v_new = int(next(it))
    w_new = int(next(it))
    new_edge = (u_new, v_new, w_new)
    
    result_indices = update_mst(n, edges, mst_edge_indices, new_edge)
    print(" ".join(str(i) for i in result_indices))

if __name__ == "__main__":
    solve()