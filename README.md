# Ford-Fulkerson Algorithm for Finding Maximum Flow in a Graph

This Python script implements the Ford-Fulkerson algorithm for finding the maximum flow from a source vertex to a sink vertex in a network flow graph.

## Description

The Ford-Fulkerson algorithm operates by repeatedly finding augmenting paths from the source to the sink in the residual graph, which is updated based on the current flow. It uses a breadth-first search (BFS) technique (implemented here with a queue) to find these paths and updates the flow along these paths until no more augmenting paths can be found.

## CustomGraph Class

The `CustomGraph` class represents a network flow graph and provides methods to compute the maximum flow using the Ford-Fulkerson algorithm.

### Methods

- `__init__(self, graph)`: Initializes the graph with the given adjacency matrix representing capacities.
- `bfs(self, start, end, parent)`: Performs a BFS to find an augmenting path from `start` to `end` and updates the `parent` array.
- `find_max_flow(self, source, sink)`: Computes the maximum flow from `source` to `sink` using the Ford-Fulkerson algorithm.

### Example Usage

```python
from collections import deque

class CustomGraph:
    def __init__(self, graph):
        self.graph = graph
        self.num_vertices = len(graph)

    def bfs(self, start, end, parent):
        visited = [False] * self.num_vertices
        queue = deque([start])
        visited[start] = True

        while queue:
            current_vertex = queue.popleft()
            for adj_vertex, capacity in enumerate(self.graph[current_vertex]):
                if not visited[adj_vertex] and capacity > 0:
                    queue.append(adj_vertex)
                    visited[adj_vertex] = True
                    parent[adj_vertex] = current_vertex
                    if adj_vertex == end:
                        return True
        return False

    def find_max_flow(self, source, sink):
        parent = [-1] * self.num_vertices
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

# Define a custom graph (adjacency matrix representing capacities)
custom_graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

# Create an instance of CustomGraph with the custom graph
my_graph = CustomGraph(custom_graph)

# Define source and sink vertices
source_vertex = 0
sink_vertex = 5

# Calculate and print the maximum possible flow
max_flow_value = my_graph.find_max_flow(source_vertex, sink_vertex)
print(f"The maximum possible flow is {max_flow_value}")
