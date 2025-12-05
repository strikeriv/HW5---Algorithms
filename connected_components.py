import sys
from collections import deque

def connected_components(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    # this problem can be solved almost in the same way as the last one
    
    # build adj array, then run BFS on each node
    # for each node, 
    adjacency_list: dict[int, list[int]] = {i: [] for i in range(n)}
    
    for edge in edges:
        u, v = edge

        # undirected graph, so we need to add to 
        # both u neighbors and v neighbors
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
        
    
    computed: set[int] = set()
    components: list[list[int]] = []
    
    for node in adjacency_list:
        if node not in computed:
            component = bfs(node, adjacency_list)
            component.sort()
            components.append(component)

            # mark nodes as visited so we don't recalculate them
            # wouldn't be in another component, but makes the same
            # component appear more than once
            for node in component:
                computed.add(node)
        
    # need to sort
    components.sort(key=lambda c: c[0])
    
    return components

def bfs(start_node: int, adjacency_list: dict[int, list[int]]) -> list[int]:
    # this BFS algo is similar to tree diagram, but here we don't care about
    # the distances, we just want a component
    
    # initialize a set of visited nodes, and a queue of nodes we process
    visited: set[int] = {start_node}
    queue: deque[int] = deque([start_node])
    
    # while the queue has nodes within
    while queue:
        # grab the next node & add to component
        curr_node = queue.popleft()
        
        # add the neighbors of the node into the que8e
        for neighbor in adjacency_list[curr_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    # simply return the nodes that were visited
    return list(visited)

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