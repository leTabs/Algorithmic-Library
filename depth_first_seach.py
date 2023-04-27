# define the DFS function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()   # create a set to store visited nodes

    visited.add(start)   # add the starting node to the visited set
    print(start, end=' ')  # print the node that is being visited

    # recursively visit the neighbors of the current node
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print(graph)
dfs(graph, 'A')
