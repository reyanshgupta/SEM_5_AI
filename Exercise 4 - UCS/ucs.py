def uniform_cost_search(goal, start):
    global graph, cost
    answer = [float('inf')] * len(goal)
    queue = [[0, start]]
    visited = set()
    count = 0

    while queue:
        queue.sort()
        p = queue.pop(0)
        p_cost, p_node = p[0], p[1]

        if p_node in goal:
            index = goal.index(p_node)

            if answer[index] == float('inf'):
                count += 1

            if answer[index] > p_cost:
                answer[index] = p_cost

        if count == len(goal):
            return answer

        if p_node not in visited:
            visited.add(p_node)
            for neighbor in graph[p_node]:
                new_cost = p_cost + cost.get((p_node, neighbor), float('inf'))
                queue.append([new_cost, neighbor])

if __name__ == '__main__':
    graph, cost = [[] for i in range(7)], {}
    graph[0].extend([1, 3])
    graph[1].append(6)
    graph[2].append(1)
    graph[3].extend([1, 4, 6])
    graph[4].extend([2, 5])
    graph[5].extend([2, 6])
    graph[6].append(4)
    cost[(0, 1)] = 2
    cost[(0, 3)] = 5
    cost[(1, 6)] = 1
    cost[(3, 1)] = 5
    cost[(3, 6)] = 6
    cost[(3, 4)] = 2
    cost[(2, 1)] = 4
    cost[(4, 2)] = 4
    cost[(4, 5)] = 3
    cost[(5, 2)] = 6
    cost[(5, 6)] = 3
    cost[(6, 4)] = 7
    goal = [6]
    answer = uniform_cost_search(goal, 0)
    print("Minimum cost from 0 to 6 is: ", answer[0])
