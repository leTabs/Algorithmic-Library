def info():
    print('-'*40)
    print('''Quick Sort has an average time complexity of O(n log n),
which makes it one of the fastest sorting algorithms available.
However, its worst-case time complexity is O(n^2), which can occur
if the pivot element is selected poorly. There are several techniques
for selecting a good pivot element to avoid worst-case behavior, such
as choosing the median of the first, middle, and last elements of the
subarray. Overall, Quick Sort is a powerful and widely used sorting algorithm.
''')
    print('-'*40)

def quick_sorting(array):
    if len(array)<=1:
        return array
    else:
        pivot = array[0]
        left  = []
        right = []
        for i in range(1, len(array)):
            if array[i] < pivot:
                left.append(array[i])
            else:
                right.append(array[i])
        return quick_sorting(left) + [pivot] + quick_sorting(right)

