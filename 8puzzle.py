from queue import PriorityQueue

class Puzzle:
    def __init__(self, board):
        self.board = board
        self.goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
        self.moves = []

    def __eq__(self, other):
        return self.board == other.board

    def __lt__(self, other):
        return self.heuristic() < other.heuristic()

    def __hash__(self):
        return hash(str(self.board))

    def find_blank(self):
        """Return the row and column index of the blank tile."""
        index = self.board.index(0)
        row = index // 3
        col = index % 3
        return row, col

    def neighbors(self):
        """Return a list of Puzzle objects representing the neighboring states."""
        row, col = self.find_blank()
        neighbors = []

        for drow, dcol, move in [(-1, 0, 'up'), (0, -1, 'left'), (1, 0, 'down'), (0, 1, 'right')]:
            new_row, new_col = row + drow, col + dcol
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_board = list(self.board)
                index1 = row * 3 + col
                index2 = new_row * 3 + new_col
                new_board[index1], new_board[index2] = new_board[index2], new_board[index1]
                new_puzzle = Puzzle(tuple(new_board))
                new_puzzle.moves = self.moves + [move]
                neighbors.append(new_puzzle)

        return neighbors

    def heuristic(self):
        """Return the estimated distance to the goal."""
        distance = 0
        for i in range(9):
            if self.board[i] != self.goal[i]:
                distance += 1
        return distance

def solve_puzzle(start):
    """Solve the 8-puzzle problem using A* search."""
    start_puzzle = Puzzle(start)
    frontier = PriorityQueue()
    frontier.put(start_puzzle)
    came_from = {start_puzzle: None}
    cost_so_far = {start_puzzle: 0}

    while not frontier.empty():
        current = frontier.get()

        if current.board == current.goal:
            return current.moves

        for neighbor in current.neighbors():
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + neighbor.heuristic()
                frontier.put(neighbor, priority)
                came_from[neighbor] = current

    return None
