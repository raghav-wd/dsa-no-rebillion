graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

graph = {
    0: [1, 4],
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3]
}

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [4],
    3: [],
    4: []
}

# def bfs(graph, start):
#     visited = set()
#     queue = [start]
#     index = 0

#     while len(queue) > index:
#         vertex = queue[index]
#         index += 1
#         if vertex not in visited:
#             visited.add(vertex)
#             print(vertex)
#             for neighbor in graph[vertex]:
#                 queue.append(neighbor)

#     return visited

# bfs(graph, 3)

def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    distance = {start: 0}
    parent = {start: None}
    index = 0

    while len(queue) > index:
        vertex = queue[index]
        index += 1
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                distance[neighbor] = 1 + distance[vertex]
                parent[neighbor] = vertex
                visited.add(neighbor)
                print(neighbor)
                queue.append(neighbor)

    return queue

# def bfs(graph, start):
#     visited = set()
#     queue = [start]
#     distance = {start: 0}
#     index = 0

#     while len(queue) > index:
#         vertex = queue[index]
#         index += 1
#         if vertex not in visited:
#             # print(vertex)
#             visited.add(vertex)
#             for neighbor in graph[vertex]:
#                 if neighbor not in visited:
#                   distance[neighbor] = 1 + distance[vertex]
#                 #   queue.append(neighbor)
#             queue.extend(graph[vertex])

#     return distance

print(bfs(graph, 0))
