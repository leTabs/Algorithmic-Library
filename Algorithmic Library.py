# -- ALGORITHMIC LIBRARY--
alg_types =[
'Searching',
'Sorting'
]
index = 1

def search():
    from Searching_algorithms import all_searchings
    return  all_searchings()
def sorting():
    print('here will be the sortings')

alg_imports =[
    search,
    sorting
]


print('Types of Algorithms')
print('-'*40)
for type in alg_types:
    print(f'{index}) {type} Algorithms')
    index += 1
print('-'*40)

#----------------------------------------------
type_choice = int(input('Number: ')) - 1
print()
print(f'The {alg_types[type_choice]} are:')
print()
alg_imports[type_choice]()
