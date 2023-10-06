class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.parent = None
        self.g = float('inf')

    def __repr__(self):
        return f"Node({self.name})"

def a_star_search(start, goal):
    open_list = []
    closed_set = set()

    start.g = 0
    open_list.append(start)

    def sort(node):
        return node.g + hcost(node.name, goal.name)

    while open_list:
        open_list.sort(key=sort, reverse=True)
        current = open_list.pop()

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = current.parent
            return path[::-1]

        closed_set.add(current)

        for neighbor, cost in current.neighbors.items():
            if neighbor in closed_set:
                continue

            temporary_val = current.g + cost
            if temporary_val < neighbor.g or neighbor not in open_list:
                neighbor.g = temporary_val
                neighbor.parent = current
                if neighbor not in open_list:
                    open_list.append(neighbor)

    return None

G = Node("G")
S = Node("S")
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")

S.neighbors = {A: 4, B: 2}
A.neighbors = {B: 3, C: 1}
B.neighbors = {D: 4, C: 2}
C.neighbors = {D: 1, G: 5}
D.neighbors = {G: 3}

def hcost(node_name, goal_name):
    heuristic_values = {"S": 7, "A": 5, "B": 8, "C": 4, "D": 6, "G": 0} 
    return heuristic_values[node_name]

start_node = S
goal_node = G

path = a_star_search(start_node, goal_node)
if path:
    print("Path found:")
    for node in path:
        print(node.name)
else:
    print("No path found")
