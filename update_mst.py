import sys
from collections import deque

def update_mst(
n: int,
edges: list[tuple[int, int, int]],
mst_edge_indices: list[int],
new_edge: tuple[int, int, int],
) -> list[int]:
    # start by building adj list
    adjacency_list: dict[int, list[tuple[int, int]]] = {i: [] for i in range(n)}
    _, _, w_new = new_edge

    # we want to store u & v in the adjacency list
    # no need to store the weight, as we reference
    # it in the max to find heaviest edge
    for idx in mst_edge_indices:
        u, v, _ = edges[idx]
        adjacency_list[u].append((v, idx))
        adjacency_list[v].append((u, idx))
    
    # run BFS to calculate the new eges once we add in the new edge
    new_edges = bfs(new_edge, adjacency_list)

    # since the weights are unique, the MST is unique
    # we grab the heaviest edge to see if we don't need to update the MST
    heaviest_edge_idx = max(new_edges, key=lambda idx: edges[idx][2])
    
    # if the new edge is heavier than the heaviest edge in the MST
    # we can return the tree, since no path becomes "lest cost"
    if w_new >= edges[heaviest_edge_idx][2]:
        return mst_edge_indices
    
    # we must update the MST then
    # we replace the heaviest edge in the MST with the new edge
    # as the definition of a MST that it has the lowest weight possible
    
    # to do so, we make a copy of the indicies, 
    # remove the heaviest edge, and then update 
    # with the new index of the edge
    updated = mst_edge_indices.copy()
    updated.remove(heaviest_edge_idx)

    # we can't use the heaviest index, as in the case you have the same
    # output with the orgiginal heaviest index, you would not be able
    # to tell if the MST was updated. next available index is just the one after
    # the last, which is just the len of the original edges
    new_edge_index = len(edges)
    updated.append(new_edge_index)

    return updated 

# BFS here needs to connect the start to the end (u -> v)
def bfs(new_edge: tuple[int, int, int], adjacency_list: dict[int, list[tuple[int, int]]]) -> list[int]:
    new_u, new_v, _ = new_edge
    
    # initialize parent to keep track of where we came from
    # visisted for the nodes we have visited
    # and queue for processing nodes
    parent: dict[int, tuple[int, int]] = {}
    visited: set[int] = {new_u}
    queue = deque([new_u])

    while queue:
        # grab node from queue and check if it is equal to new_v
        # if so, we have reached our end goal, so break the loop
        node = queue.popleft()
        if node == new_v:
            break
        
        # otherwise, we add the neighbors that we have not yet seen to the queue
        # and add the node plus its edge index into parent (used to backtrace)
        for neighbor, edge_idx in adjacency_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = (node, edge_idx)
                queue.append(neighbor)
    
    # now we must backtrace to rebuild the path
    # use the parent to look up it';s parent.. yada yada
    # until we get back to new_u node
    edges: list[int] = []
    node: int = new_v 
    while node != new_u:
        p_node, edge_idx = parent[node]
        edges.append(edge_idx)
        node = p_node
        
    return edges

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