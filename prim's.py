from heapq import heappop, heappush

def prim(graph, start):
    # Initialize variables
    mst = set()  # Set of edges in the minimum spanning tree
    visited = set([start])  # Set of visited vertices
    edges = [(weight, start, to) for to, weight in graph[start].items()]
    heapify(edges)

    # Loop until all edges are added to the MST
    while edges:
        weight, frm, to = heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.add((frm, to, weight))
            for to_next, weight_next in graph[to].items():
                if to_next not in visited:
                    heappush(edges, (weight_next, to, to_next))

    return mst

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 4},
    'D': {'B': 1, 'C': 4},
}

print(prim(graph, 'A'))
