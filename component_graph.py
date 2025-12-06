import sys

def component_graph(n: int, edges: list[tuple[int, int]]) -> tuple[list[int], list[tuple[int, int]]]:
    # Kosaraju's algorithm
    
    # compute times with DFS
    # build adj list to start
    adjacency_list: dict[int, list[int]] = {i: [] for i in range(n)}
        
    for edge in edges:
        u, v = edge

        adjacency_list[u].append(v)
    
    # we do DFS
    # must define these variables outside since they are needed for every iteration
    # we need a "finished order" and a visisted set
    visited: set[int] = set()
    order: list[int] = []
    
    # we run one DFS to get the order in finished time
    # doesn't matter where we start, so just do it here
    for node in range(n):
        if node not in visited:
            dfs(node, adjacency_list, visited, order)
    
    # Kosaraju's algorithm requires we run DFS again, but from the nodes that finished last
    # so, we need to transpose the graph for step 2
    transpose_adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, neighbors in adjacency_list.items():
        for v in neighbors:
            transpose_adj[v].append(u)
    
    # now we can implement step 3 and run DFS a second time
    visited.clear()
    sccs: list[list[int]] = []

    for node in reversed(order):
        if node not in visited:
            component: list[int] = []
            dfs(node, transpose_adj, visited, component)
            sccs.append(component)

    
    # now that we have the strongly connected components, we need to sort
    sccs.sort(key=lambda comp: min(comp))

    # also sort within the sccs
    for comp in sccs:
        comp.sort()
    
    # step 4 requires us to output the vertices of the tree as a
    # seperate strongly connected component
    component: list[int] = [0] * n
    
    # we build the component by connecting the sccs back to the original graph
    # really hard to explain in a comment... took me like an hour to understand
    # TLDR; if you have SCCS of [[0, 1], [2, 3], [4]], it becomes [0, 0, 1, 1, 2]
    # because we set the index of the comp from the ssc value to the id of the ssc
    for component_id, comp in enumerate(sccs):
        for vertex in comp:
            component[vertex] = component_id
    
    # now that we have the component built, we build the graph edges
    # component tells us what vertex are connected to one another
    # so, we now build the actual edges between our sccs above from the original graph
    component_edges: set[tuple[int, int]] = set()
    for edge in edges:
        u, v = edge
        
        comp_u = component[u]
        comp_v = component[v]
        
        # we only say it's a component if the vertexes are in different sccs
        # so, compare the vertexes they are connected to
        # if they are different, then that is an edge to another component
        if comp_u != comp_v:
            component_edges.add((comp_u, comp_v))
    
    comp_edges = list(component_edges)
    comp_edges.sort(key=lambda x: (x[0], x[1]))
    
    return component, comp_edges

# Kosaraju's requires DFS
def dfs(start_node: int, adjacency_list: dict[int, list[int]], visited: set[int], order: list[int]) -> None:
    visited.add(start_node)
    
    # DFS returns the order in which it takes to visit and explore each neighbor
    # when this function finishes, the order will be in order of "finishing time"
    for node in adjacency_list[start_node]:
        if node not in visited:
            dfs(node, adjacency_list, visited, order)
    order.append(start_node)

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