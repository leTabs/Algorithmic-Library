# Searching Algorithms #
#import time
searchings = [
'Linear',
'Binary'
]
def linear(array, target):
    from linear_search import info, linear_search
    info()
    print(linear_search(array, target))

def binary(array, target):
    from binary_search import info, binary_search
    info()
    print(binary_search(array, target))

search_imports =[
    linear,
    binary
]

def all_searchings():
    index = 1
    for alg in searchings:
        print(f'{index}) {alg} Algorithm')
        index +=1
    search_choice = int(input('Number: ')) - 1
    print()
    #print(searchings[search_choice])
    arr = input('Enter the array: ')
    tar = input('Enter the target: ')
    list_comp = ['[', ']', '"', "'", ' ']
    for comp in list_comp:
        arr = arr.replace(comp, '')
    arr = arr.split(',')
    search_imports[search_choice](arr, tar)
#all_searchings()
