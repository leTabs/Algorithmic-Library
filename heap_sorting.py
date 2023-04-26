def info():
    print('-'*40)
    print('''Heap Sort has a time complexity of O(n log n), which makes it one of
the fastest sorting algorithms available. However, it is not as widely
used as some other sorting algorithms because it is not stable (meaning
that it does not preserve the relative order of equal elements in the
original array) and because it requires building the binary heap data
structure, which can be costly. Overall, Heap Sort is a powerful and
efficient sorting algorithm in certain situations.
''')
    print('-'*40)

def heap_sorting(array):
    proxy_array = []
    for i in range(len(array)):
        proxy_array.append(min(array))
        array.remove(min(array))

    array = proxy_array[:]
    return array
