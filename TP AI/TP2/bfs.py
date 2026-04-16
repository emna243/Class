def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        etat = queue.pop(0)  # pop from the front for BFS
        if etat not in visited:
            visited.insert(len(visited), etat)  # add to visited list
            # Add unvisited neighbors to the queue
            for neighbor in graph.get(etat, set()):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return visited

graph = {
    'a': set(['b', 'c']),
    'b': set(['d', 'e']),
    'c': set(['f', 'g']),
    'e': set(['h'])
}

result = bfs(graph, 'a')
print(result)