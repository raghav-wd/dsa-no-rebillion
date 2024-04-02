graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

graph = {
    0: [1, 2, 3],
    1: [0, 4],
    2: [0, 1],
    3: [0],
    4: [1]
}

graph = {
    0: [2, 3],
    1: [0, 4],
    2: [1],
    3: [],
    4: []
}

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [4],
    3: [],
    4: []
}

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            stack.extend(graph[vertex])

def bfs(graph, start):
    visited = set()
    queue = [start]
    idx = 0

    while idx < len(queue):
        vertex = queue[idx]
        idx = idx + 1
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        
    print(queue)

bfs(graph, 0)


