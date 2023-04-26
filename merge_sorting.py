def info():
    print('-'*40)
    print('''Merge Sort has a time complexity of O(n log n),
which makes it one of the fastest sorting algorithms
available. It is also a stable sorting algorithm, meaning
that it preserves the relative order of equal elements in
the original array. Additionally, Merge Sort is a useful
algorithm for sorting linked lists, as it can be implemented
to run in O(1) space complexity. Overall, Merge Sort is
a powerful and widely used sorting algorithm.
''')
    print('-'*40)


def merge_sorting(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sorting(left_half)
        merge_sorting(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr
