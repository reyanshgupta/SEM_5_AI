class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items)==0
    
def DFS(graph,start):
    visited=set()
    stack  = Stack()
    stack.push(start)
    
    while not stack.is_empty():
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex,end=' ')
            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    stack.push(neighbour)
                    
graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : ['3'],
    '4' : ['8'],
    '8' : [],
}

print("DFS with stack: ")
DFS(graph,'5')