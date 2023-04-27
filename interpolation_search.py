def info():
    print('-'*40)
    print('''Overall, the Interpolation Search algorithm has an average time
complexity of O(log(log(n))) when the data is uniformly distributed,
which makes it faster than the Binary Search algorithm. However, in
''')
    print('-'*40)

def interpolation_search(array, target):
    array = sorted(array)
    n = len(array)
    low = 0
    high = n - 1

    while low <= high and target >= array[low] and target <= array[high]:
        index = low + ((target - array[low]) * (high - low)) // (array[high] - array[low])

        if array[index] == target:
            return (f'Target "{target}" found in:  {index}th position.')

        if array[index] < target:
            low = index + 1
        else:
            high = index - 1
    return (f'Target "{target}" is not located in the array.')
