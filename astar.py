def a_star(start, goal, graph):
    open_set = {start}
    closed_set = set()
    g_score = {start: 0}
    parents = {start: None}
    
    while open_set:
        current = min(open_set, key=lambda x: g_score[x] + heuristic(x, goal))
        
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = parents[current]
            path.append(start)
            path.reverse()
            return path
        
        open_set.remove(current)
        closed_set.add(current)
        
        for neighbor, weight in graph[current]:
            tentative_g_score = g_score[current] + weight
            if neighbor in closed_set:
                continue
            if neighbor not in open_set or tentative_g_score < g_score[neighbor]:
                parents[neighbor] = current
                g_score[neighbor] = tentative_g_score
                if neighbor not in open_set:
                    open_set.add(neighbor)
                    
    return None

def heuristic(node, goal):
    h_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0
    }
    return h_dist[node]

graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'D': [('G', 1)],
    'E': [('D', 6)],
    'G': []
}

path = a_star('A', 'G', graph)
print(path)
