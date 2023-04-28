# Write your code here :-)
def info():
    print('-'*40)
    print('''
    Breadth First Search
''')
    print('-'*40)

from collections import deque

def bfs(array, target):
    visited = set()
    queue = deque([target])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)
            print(vertex)

            for neighbor in array[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
