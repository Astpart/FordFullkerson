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


# Define a custom graph
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

# Define source and sink
source_vertex = 0
sink_vertex = 5

# Calculate and print the maximum possible flow
max_flow_value = my_graph.find_max_flow(source_vertex, sink_vertex)
print(f"The maximum possible flow is {max_flow_value}")
