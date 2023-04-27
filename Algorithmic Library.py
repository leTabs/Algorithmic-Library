# -- ALGORITHMIC LIBRARY--
import sys

alg_types =[
'Searching',
'Sorting'
]

index = 1
print('Types of Algorithms')
print('-'*40)
for type in alg_types:
    print(f'{index}) {type} Algorithms')
    index += 1
print('-'*40)

def search():
    from Searching_algorithms import all_searchings
    return  all_searchings()
def sorting():
    from Sorting_algorithms import all_sortings
    return all_sortings()

alg_imports =[
    search,
    sorting
]
#----------------------------------------------
type_choice = int(input('Number: ')) - 1
print()
print(f'The {alg_types[type_choice]} are:')
print()
alg_imports[type_choice]()

# remeber to add searching in the searchin algorithms .py

close = input(':')
sys.exit()
