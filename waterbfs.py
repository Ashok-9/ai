from collections import deque

def water_jug_bfs(start, target, sizes):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == target:
            return path
        if state in visited:
            continue
        visited.add(state)
        for move in ['fill A', 'fill B', 'empty A', 'empty B', 'A to B', 'B to A']:
            if move == 'fill A':
                new_state = (sizes[0], state[1])
            elif move == 'fill B':
                new_state = (state[0], sizes[1])
            elif move == 'empty A':
                new_state = (0, state[1])
            elif move == 'empty B':
                new_state = (state[0], 0)
            elif move == 'A to B':
                amount = min(state[0], sizes[1] - state[1])
                new_state = (state[0] - amount, state[1] + amount)
            elif move == 'B to A':
                amount = min(sizes[0] - state[0], state[1])
                new_state = (state[0] + amount, state[1] - amount)
            else:
                continue
            queue.append((new_state, path + [move]))
    return None
# Example input:
start = (0, 0)   # initial state of jugs A and B
target = (4, 0)  # goal state of jug A having 4 liters of water
sizes = (7, 5)   # sizes of jugs A and B, respectively

# Call the function:
path = water_jug_bfs(start, target, sizes)

# Print the result:
print(path)
