graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : ['3'],
    '4' : ['8'],
    '8' : [],
}
visited = set()
def DFS(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        #if neighbour not in dfs, we recurse through nodes
        for neighbour in graph[node]:
            DFS(visited,graph,neighbour)
        
print("DFS For starting node 5: ")
DFS(visited, graph, '5')