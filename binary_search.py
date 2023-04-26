# the Binary Search Algorithm
def info():
    print('-'*40)
    print('''
Binary search is a classic algorithm used for searching
sorted arrays efficiently.
The algorithm works by repeatedly
dividing the search interval in half
until the target value is found or
determined to be not in the array.
To perform a binary search, we start
by comparing the target value with
the middle element of the array.
If the target value is less than
the middle element, we discard
the upper half of the array,
and the search continues in
the lower half. If the target
value is greater than the middle
element, we discard the lower half,
and the search continues in the upper
half. This process is repeated until
the target value is found, or the search interval is empty.
Binary search has a time complexity of O(log n), which is significantly
faster than linear search (O(n)), making it a useful algorithm for large
datasets. However, it requires that the array be sorted, which may be a
disadvantage in some cases.
''')
    print('-'*40)

def binary_search(array, target):
    starting_index = 0
    ending_index = len(array) - 1
    if target not in array:
        return (f'The target "{target}" is not in the array')
        # informs the user if the target is stored in the array
    while True:
        # while loop so that we have as many iterations as needed
        middle_index = (starting_index + ending_index) // 2
        # calculate the middle index of the array at the beggining of each iteration

        if target < array[middle_index]:
            ending_index = middle_index - 1
            # if the condition is true then the array is sliced and the right half is discarded

        if target > array[middle_index]:
            starting_index = middle_index + 1
            # if the condition is true then the array is sliced and the left half is discarded

        if target == array[middle_index]:
            # the iterations keep hapening until this condition is true
            return f'Target "{target}" found in:  {middle_index}th position.'
            # the desired index is being return and the function terminates
