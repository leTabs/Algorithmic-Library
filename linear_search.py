def info():
    print('-'*40)
    print('''The linear search algorithm
is a simple and straightforward approach
to finding a specific value in a list or
array of data. It works by sequentially
checking each element in the list until
the desired value is found or until the
end of the list is reached. Although it
may not be the most efficient search algorithm
for large datasets, it is easy to implement
and can be used for small datasets or when
the data is not sorted. The time complexity
of the linear search algorithm is O(n), where
n is the number of elements in the list.
''')
    print('-'*40)


def linear_search(array, target):

    index = 0
    for item in array:
        if item == target:
            return (f'Target "{target}" found in:  {index}th position.')
        index += 1
        if index == len(array):
            return (f'Target "{target}" is not located in the array.')
