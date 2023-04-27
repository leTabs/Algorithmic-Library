# Sorting Algorithms #
#import time
sortings = [
'Bubble',
'Selection',
'Insertion',
'Merge',
'Quick',
'Heap',
'Counting',
'Radix',
'Bucket',
'Shell'
]
def bubble(array):
    from sorting.bubble_sorting import info, bubble_sorting
    info()
    print(bubble_sorting(array))
def selection(array):
    from sorting.selection_sorting import info, selection_sorting
    info()
    print(selection_sorting(array))
def insertion(array):
    from sorting.insertion_sorting import info, insertion_sorting
    info()
    print(insertion_sorting(array))
def quick(array):
    from sorting.quick_sorting import info, quick_sorting
    info()
    print(quick_sorting(array))
def heap(array):
    from sorting.heap_sorting import info, heap_sorting
    info()
    print(heap_sorting(array))
def merge(array):
    from sorting.merge_sorting import info, merge_sorting
    info()
    print(merge_sorting(array))
def counting(array):
    from sorting.counting_sorting import info, counting_sorting
    info()
    print(counting_sorting(array))
def radix(array):
    from sorting.radix_sorting import info, radix_sorting
    info()
    print(radix_sorting(array))
def bucket(array):
    from sorting.bucket_sorting import info, bucket_sorting
    info()
    print(bucket_sorting(array))
def shell(array):
    from sorting.shell_sorting import info, shell_sorting
    info() # i can probably change this two calls in to a one-liner
    print(shell_sorting(array))


sort_imports =[
    bubble,
    selection,
    insertion,
    merge,
    quick,
    heap,
    counting,
    radix,
    bucket,
    shell
]

def all_sortings():
    index = 1
    for alg in sortings:
        print(f'{index}) {alg} Sorting Algorithm')
        index +=1
    print('-'*40)
    sort_choice = int(input('Number: ')) - 1
    print()
    #------------------------------------------
    arr = input('Enter the array: ')
    list_comp = ['[', ']', '"', "'", ' ']
    for comp in list_comp:
        arr = arr.replace(comp, '')
    arr = arr.split(',')
    try:
        for i in range(len(arr)):
            arr[i] = int(arr[i])
            # fix this to return the original ones
    except ValueError: pass
    #------------------------------------------
    sort_imports[sort_choice](arr)
