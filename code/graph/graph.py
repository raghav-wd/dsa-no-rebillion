class Graph:
    def __init__(self, vertices):
        # self.adjList = [None] * (vertices + 1)
        self.adjList = [None] * (vertices + 1)
        for i in range(0, vertices + 1):
            self.adjList[i] = []
    
    def addEdge(self, vertice, edge):
        self.adjList[vertice].append(edge)

        self.adjList[edge].append(vertice)

    def getGraph(self):
        return self.adjList
    

graph = Graph(3)
graph.addEdge(2, 3)
# graph.addEdge(2, 3)

graph = graph.getGraph()
# graph[1].append(1)

print(graph)