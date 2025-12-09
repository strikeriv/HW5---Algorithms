import sys

def early_bellman_ford(
n: int,
edges: list[tuple[int, int, int]],
s: int
) -> list[float]:
    # we initialize single source paths
    distances: dict[int, float] = {}
    predecesors:  dict[int, int | None] = {}
    
    for v in range(n):
        distances[v] = float("inf") # infinity from solve (didn't know this was a thing)
        predecesors[v] = None
    
    # distance for source starts at 0
    distances[s] = 0
    
    # we now relax the edges
    # normally, BF does not have the any_chanced logic, but to implement early BF we need it
    # every iteration of _ through n, we relax each edge. if no edges changed, no need to continue
    # as we have gone through the maximum distance length, so we can just end early
    for _ in range(n - 1):
        any_changed = False
        
        for edge in edges:
            edge_changed = relax(edge, distances, predecesors)
            any_changed = any_changed or edge_changed # must do it this way to break correctly
            
        if not any_changed:
            break
            
    return [distances[v] for v in range(n)] # converrt the dict values to a list

# follows the book algorithm 1-1, except we return True / False
# if the distances & predecessors were updated (path was shorter)
def relax(edge: tuple[int, int, int], distances: dict[int, float], predecessors:  dict[int, int | None]) -> bool:
    u, v, w = edge
    
    distance_u = distances[u]
    distance_v = distances[v]

    if distance_v <= distance_u + w:
        return False
    
    distances[v] = distance_u + w
    predecessors[v] = u
    
    return True

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