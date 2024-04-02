def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)  # or do whatever operation you want with the vertex
            for neighbor in graph[vertex]:
                stack.append(neighbor)
            # OR
            # stack.extend(graph[vertex])

    return visited

# Example graph represented as an adjacency list
# graph = {
#     'a': {'b', 'd'},
#     'b': {'c'},
#     'c': {'d', 'f', 'e'},
#     'd': {},
#     'e': {},
#     'f': {'e'}
# }
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')