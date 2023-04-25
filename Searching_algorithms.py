# Searching Algorithms #
searchings = [
'Linear',
'Binary'
]
def linear(array, target):
    from linear_search import introduction, linear_search
    introduction()
    print(linear_search(array, target))

search_imports =[
    linear
]

def all_searchings():
    index = 1
    for alg in searchings:
        print(f'{index}) {alg} Algorithm')
        index +=1
    search_choice = int(input('Number: ')) - 1
    print()
    #print(searchings[search_choice])
    search_imports[search_choice](['t', 'a'], 'ar')
all_searchings()
