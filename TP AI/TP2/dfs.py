def dfs(graph, start):
    visited = []
    stack = [start]  # Use stack (LIFO) instead of queue
    while stack:
        etat = stack.pop()  # pop from the end for DFS
        if etat not in visited:
            visited.append(etat)  # add to visited list
            # Add unvisited neighbors to the stack
            for neighbor in graph.get(etat, set()):
                if neighbor not in visited and neighbor not in stack:
                    stack.append(neighbor)
    return visited

graph = {
    'a': set(['b', 'c']),
    'b': set(['d', 'e']),
    'c': set(['f', 'g']),
    'e': set(['h'])
}

result = dfs(graph, 'a')
print(result)