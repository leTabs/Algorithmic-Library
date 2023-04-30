
INF = float('inf')

def bellman_ford(graph, start):
    # Initialize distances
    distances = {}
    for vertex in graph:
        distances[vertex] = INF
    distances[start] = 0

    # Relax edges repeatedly
    for i in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] != INF and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    # Check for negative-weight cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] != INF and distances[u] + weight < distances[v]:
                raise Exception("Negative-weight cycle detected")

    return distances

g = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 4},
    'C': {'B': 1, 'D': 1},
    'D': {}
}
print(bellman_ford(g, 'A'))
