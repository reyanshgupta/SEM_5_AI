graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : ['3'],
    '4' : ['8'],
    '8' : [],
}

visited = []
queue = []

def BFS(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        elem = queue.pop(0)
        print(elem, end=' ')

        for neighbour in graph[elem]:
            if neighbour not in visited:  # Check if the neighbor has already been visited
                visited.append(neighbour)
                queue.append(neighbour)

print("BFS:")
BFS(visited, graph, '5')
