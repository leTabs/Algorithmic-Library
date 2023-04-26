# selection sorting algorithm
def info():
    print('-'*40)
    print('''Selection Sort has a time complexity of O(n^2),
which makes it less efficient than more advanced sorting
algorithms such as Quick Sort and Merge Sort. However, it
has the advantage of requiring only one swap per iteration,
making it a useful algorithm for small datasets or for situations
where memory usage is a concern. Additionally, it is simple to
implement and understand, making it a useful tool for teaching
the basics of sorting algorithms.
''')
    print('-'*40)
def selection_sorting(array):
    for item in range(len(array)):
        min_item = min(array[item:])
        min_index = array.index(min_item, item)
        if min_item < array[item]:
            array[item] , array[min_index] = array[min_index], array[item]
    return array
