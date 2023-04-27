def info():
    print('-'*40)
    print('''
Fibonacci search algorithm
''')
    print('-'*40)

def fibonacci_search(array, target):
    array = sorted(array)
    n = len(array)
    fibM = 0
    fibM1 = 1
    fibM2 = fibM + fibM1
    while fibM2 < n:
        fibM = fibM1
        fibM1 = fibM2
        fibM2 = fibM + fibM1
    offset = -1
    while fibM2 > 1:
        index = min(offset + fibM, n - 1)
        if array[index] < target:
            fibM2 = fibM1
            fibM1 = fibM
            fibM = fibM2 - fibM1
            offset = index
        elif array[index] > target:
            fibM2 = fibM
            fibM1 = fibM1 - fibM
            fibM = fibM2 - fibM1
        else:
            return (f'Target "{target}" found in:  {index}th position.')
    return (f'Target "{target}" is not located in the array.')
