def info():
    print('-'*40)
    print('''Insertion Sort has a time complexity of O(n^2),
which makes it less efficient than more advanced sorting
algorithms such as Quick Sort and Merge Sort. However, it
is efficient for small datasets and has the advantage of
being an "in-place" sorting algorithm, meaning it does not
require additional memory for sorting. Additionally, it is
simple to implement and understand, making it a useful tool
for teaching the basics of sorting algorithms.
''')
    print('-'*40)
def insertion_sorting(array):
    if array[0]>array[1]:
        array[0], array[1] = array[1], array[0]
    for i in range(2, len(array)):
        for r in range(len(array[:i]), 0, -1):
            if array[i] < array[r-1]:
                array[i], array[r-1] = array[r-1], array[i]
                i-=1
    return array
