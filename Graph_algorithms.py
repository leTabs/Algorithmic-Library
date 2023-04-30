import ast
graphings = [
    'Dijkstra\'s',
    'Bellman Ford',
]
def dijkstra(graph, start):
    from graphs.dijkstras import dijkstra
    print(dijkstra(graph, start))
def bellman_ford(graph, start):
    from graphs.bellman_ford import bellman_ford
    print(bellman_ford(graph, start))
graph_imports = [
    dijkstra,
    bellman_ford
]

def all_graphings():
    index = 1
    for alg in graphings:
        print(f'{index}) {alg} Algorithm')
        index +=1
    print('-'*40)
    graph_choice = int(input('Number: ')) - 1
    print()
    #------------------------------------------
    graph = input("Enter an list/ dictionary: ")
    graph = ast.literal_eval(graph)
    start = input('Enter the target: ')
    try:
        start = int(start)
    except ValueError: pass
    #------------------------------------------
    graph_imports[graph_choice](graph, start)
