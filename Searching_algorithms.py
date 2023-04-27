# Searching Algorithms #
#import time
searchings = [
'Linear',
'Binary',
'Jump',
'Interpolation',
'Exponential',
'Fibonacci',
'Ternary'
]
def linear(array, target):
    from searching.linear_search import info, linear_search
    info()
    print(linear_search(array, target))

def binary(array, target):
    from searching.binary_search import info, binary_search
    info()
    print(binary_search(array, target))
def jump(array, target):
    from searching.jump_search import info, jump_search
    info()
    print(jump_search(array, target))
def interpolation(array, target):
    from searching.interpolation_search import info, interpolation_search
    info()
    print(interpolation_search(array, target))
def exponential(array, target):
    from searching.exponential_search import info, exponential_search
    info()
    print(exponential_search(array, target))
def fibonacci(array, target):
    from  searching.fibonacci_search import info, fibonacci_search
    info()
    print(fibonacci_search(array, target))
def ternary(array, target):
    from searching.ternary_search import info, ternary_search
    info()
    print(ternary_search(array, target))
search_imports =[
    linear,
    binary,
    jump,
    interpolation,
    exponential,
    fibonacci,
    ternary
]

def all_searchings():
    index = 1
    for alg in searchings:
        print(f'{index}) {alg} Algorithm')
        index +=1
    print('-'*40)
    search_choice = int(input('Number: ')) - 1
    print()
    #print(searchings[search_choice])
    #------------------------------------------
    arr = input('Enter the array: ')
    try:
        tar = int(input('Enter the target: '))
    except ValueError: pass
    list_comp = ['[', ']', '"', "'", ' ']
    for comp in list_comp:
        arr = arr.replace(comp, '')
    arr = arr.split(',')
    try:
        for i in range(len(arr)):
            arr[i] = int(arr[i])
            # fix this to return the original ones
    except ValueError: pass
    #-----------------------
    search_imports[search_choice](arr, tar)
#all_searchings()
