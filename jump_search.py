import math


def info():
    print('-'*40)
    print('''
Jump search is similar to binary search in terms of time complexity,
but it is more suitable for larger arrays where the cost of sorting
the array is high. It also performs better than linear search for large
arrays because it reduces the number of comparisons needed to find the
target value. However, it may not perform as well as other searching
algorithms such as interpolation search or exponential search in certain cases.
''')
    print('-'*40)

def jump_search(array, target):
    array = sorted(array)
    n = len(array)
    # Finding the block size to jump
    step = int(math.sqrt(n))
    # Finding the block where target exists (if present)
    index = 0
    while array[min(step, n)-1] < target:
        index = step
        step += int(math.sqrt(n))
        if index >= n:
            return -1
    # Doing a linear search for target in the block starting with prev
    while array[index] < target:
        index += 1
        if index == min(step, n):
            return -1
    if array[index] == target:
        return (f'Target "{target}" found in:  {index}th position.')
    return (f'Target "{target}" is not located in the array.')
