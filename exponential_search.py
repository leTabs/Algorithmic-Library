def info():
    print('-'*40)
    print('''The exponential search algorithm is based on the principle
of dividing the search interval by two in each iteration, so
that the search interval is exponentially reduced until the
target value is found or the interval size becomes 1.
''')
    print('-'*40)


def exponential_search(array, target):
    n = len(array)
    if array[0] == target:
        return 0
    i = 1
    while i < n and array[i] <= target:
        i = i * 2
    return binary_search(array, i // 2, min(i, n - 1), target)

def binary_search(array, l, r, target):
    while l <= r:
        index = l + (r - l) // 2
        if array[index] == target:
            return  (f'Target "{target}" found in:  {index}th position.')
        elif array[index] < target:
            l = index + 1
        else:
            r = index - 1
    return (f'Target "{target}" is not located in the array.')
