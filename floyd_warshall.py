# Define infinity as a very large number
def info():
    print('-'*40)
    print('''
    Floyd WarShall
''')
    print('-'*40)
# deal with this lter alright??????????



#inf = float('inf')
import ast
# Function to implement the Floyd-Warshall algorithm
def floyd_warshall(graph):
    info()
    n = len(graph)
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
graph = input("Enter an list/ dictionary: ")
for i in graph:
    if type(i) != int:
        i = float('inf')
#graph = ast.literal_eval(graph)
# Example usage


print(floyd_warshall(graph))
