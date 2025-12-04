import sys
from collections import deque

def tree_diameter(n: int, edges: list[tuple[int, int]]) -> int:
    # we can solve this problem quite easily
    # a property of graphs is that we can run BFS from any node, 
    # and the longest path is guarenteed to be at an end of the tree
    
    # so, run BFS on the first edge in the array.
    # then, by the same principle, run BFS again from that node. 
    # diameter is the length of that path
    
    # now we start. BFS time!
    # build an adjacency dictionary
    adjacency_list: dict[int, list[int]] = {i: [] for i in range(n)}
    
    for edge in edges:
        u, v = edge

        # undirected graph, so we need to add to 
        # both u neighbors and v neighbors
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
        
    # run BFS to get furthest from start node
    first_furthest = bfs(0, adjacency_list)
    
    # run BFS again to get furthest node from first farthest
    second_furthest = bfs(first_furthest[0], adjacency_list)

    return second_furthest[1] # distance is diameter

def bfs(start_node: int, adjacency_list: dict[int, list[int]]) -> tuple[int, int]:
    
    # store the max distance and the node that is at that distance
    max_distance = 0
    farthest: tuple[int, int] = (start_node, 0)
    
    # initialize a set of visited nodes, and a queue of nodes we process
    visited: set[int] = {start_node}
    queue: deque[tuple[int, int]] = deque([farthest])
    
    # while the queue has nodes within
    while queue:
        # grab the next node & deconstruct
        curr = queue.popleft()
        curr_node, curr_distance = curr
        
        # see if the node longer than max distance
        # if so, it's the new longest path, so update as accordingly
        if curr_distance > max_distance:
            max_distance = curr_distance
            farthest = curr
        
        # add the neighbors of the node into the list
        for neighbor in adjacency_list[curr_node]:
            # check if it's already been visited
            # prevents useless computing & infinite since we'd be 
            # going backwards & would compute the same node again
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, curr_distance + 1))
    
    # simply return farthest & max distance computed
    return (farthest[0], max_distance)

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
    ans = tree_diameter(n, edges)
    print(ans)
        
if __name__ == "__main__":
    solve()