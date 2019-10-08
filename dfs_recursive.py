def dfs_recursive(graph, vertex, visited=[]):
    visited += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            visited = dfs_recursive(graph, neighbor, visited)

    return visited


adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

print(dfs_recursive(adjacency_matrix, 1))
