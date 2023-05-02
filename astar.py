import heapq

def a_star(start, goal, graph_nodes, h_dist):
    pq = [(0, start, [])]
    visited = set()
    
    while pq:
        dist, node, path = heapq.heappop(pq)
        
        if node == goal:
            return path + [node]
        
        if node in visited:
            continue
            
        visited.add(node)
        
        for neighbor, neighbor_dist in graph_nodes.get(node, []):
            if neighbor not in visited:
                f = dist + neighbor_dist + h_dist[neighbor]
                heapq.heappush(pq, (f, neighbor, path + [node]))
    
    return None


graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)],
}

h_dist = {
    'A': 11,
    'B': 1,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0,
}

start = "A"
goal = "G"

path = a_star(start, goal, graph_nodes, h_dist)

if path:
    print(" -> ".join(path))
else:
    print("No path found.")

