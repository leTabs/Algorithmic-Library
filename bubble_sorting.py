def info():
    print('-'*40)
    print('''Bubble Sort has a time complexity of O(n^2),
which means that it is not very efficient for large arrays.
However, it is easy to implement and understand, making it
a useful tool for teaching the basics of sorting algorithms.
''')
    print('-'*40)
def bubble_sorting(array):
    for i in range(len(array)):
        for item in range(len(array)-i-1):
            if array[item]>array[item+1]:
                array[item], array[item+1] = array[item+1], array[item]
    return array
