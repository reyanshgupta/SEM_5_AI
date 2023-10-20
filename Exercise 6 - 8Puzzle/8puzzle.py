from queue import PriorityQueue

class Puzzle:
    def __init__(self, board, goal):
        self.board = board
        self.goal = goal
        self.moves = []
        self.parent = None
        self.depth = 0
    
    def get_blank_pos(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
    
    def get_children(self):
        children = []
        row, col = self.get_blank_pos()
        
        if row > 0:
            new_board = [row[:] for row in self.board]
            new_board[row][col], new_board[row-1][col] = new_board[row-1][col], new_board[row][col]
            child = Puzzle(new_board, self.goal)
            child.moves = self.moves + ['U']
            child.parent = self
            child.depth = self.depth + 1
            children.append(child)
        
        if row < 2:
            new_board = [row[:] for row in self.board]
            new_board[row][col], new_board[row+1][col] = new_board[row+1][col], new_board[row][col]
            child = Puzzle(new_board, self.goal)
            child.moves = self.moves + ['D']
            child.parent = self
            child.depth = self.depth + 1
            children.append(child)
        
        if col > 0:
            new_board = [row[:] for row in self.board]
            new_board[row][col], new_board[row][col-1] = new_board[row][col-1], new_board[row][col]
            child = Puzzle(new_board, self.goal)
            child.moves = self.moves + ['L']
            child.parent = self
            child.depth = self.depth + 1
            children.append(child)
        
        if col < 2:
            new_board = [row[:] for row in self.board]
            new_board[row][col], new_board[row][col+1] = new_board[row][col+1], new_board[row][col]
            child = Puzzle(new_board, self.goal)
            child.moves = self.moves + ['R']
            child.parent = self
            child.depth = self.depth + 1
            children.append(child)
        
        return children
    
    def move(self, direction):
        row, col = self.get_blank_pos()
        
        if direction == 'U':
            self.board[row][col], self.board[row-1][col] = self.board[row-1][col], self.board[row][col]
        
        elif direction == 'D':
            self.board[row][col], self.board[row+1][col] = self.board[row+1][col], self.board[row][col]
        
        elif direction == 'L':
            self.board[row][col], self.board[row][col-1] = self.board[row][col-1], self.board[row][col]
        
        elif direction == 'R':
            self.board[row][col], self.board[row][col+1] = self.board[row][col+1], self.board[row][col]
    
    def is_goal(self):
        return self.board == self.goal
    
    def solve(self):
        frontier = PriorityQueue()
        frontier.put((0, id(self), self))
        explored = set()
        
        while not frontier.empty():
            x, y, node = frontier.get()
            
            if node.is_goal():
                moves = []
                while node.parent is not None:
                    moves.append(node.moves[-1])
                    node = node.parent
                moves.reverse()
                return moves
            
            explored.add(id(node))
            
            for child in node.get_children():
                if id(child) not in explored:
                    priority = child.depth + self.heuristic(child)
                    frontier.put((priority, id(child), child))
        
        return None
    
    def heuristic(self, node):
        count = 0
        for i in range(3):
            for j in range(3):
                if node.board[i][j] != self.goal[i][j]:
                    count += 1
        return count
    
initial_board = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
initial_puzzle = Puzzle(initial_board, goal_state)
solution = initial_puzzle.solve()
if solution is not None:
    print("Solution found! Moves to reach the goal:")
    print(solution)
else:
    print("No solution found.")
