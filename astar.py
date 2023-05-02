from queue import PriorityQueue

def a_star(start, goal, neighbors_func, heuristic_func):

    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor in neighbors_func(current):
            new_cost = cost_so_far[current] + heuristic_func(current, neighbor)
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic_func(goal, neighbor)
                frontier.put(neighbor, priority)
                came_from[neighbor] = current

    return None
start = 'A'
goal = 'E'

# A dictionary of neighbors for each node
neighbors = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 2},
    'E': {'D': 2}
}

# A dictionary of estimated distances between nodes
heuristic = {
    'A': 4,
    'B': 2,
    'C': 4,
    'D': 1,
    'E': 0
}

# Call the function
path = a_star(start, goal, lambda node: neighbors[node], lambda node1, node2: heuristic[node2])
