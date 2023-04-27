def info():
    print('-'*40)
    print('''
Ternary
''')
    print('-'*40)

def ternary_search(array, target):
    array = sorted(array)
    left = 0
    right = len(array) - 1

    while left <= right:
        # Calculate the two split points
        split1 = left + (right - left) // 3
        split2 = right - (right - left) // 3

        # Check if the target is at one of the split points
        if array[split1] == target:
            return (f'Target "{target}" found in:  {split1}th position.')
        elif array[split2] == target:
            return  (f'Target "{target}" found in:  {split2}th position.')

        # If the target is not at one of the split points, update the search range
        elif target < array[split1]:
            right = split1 - 1
        elif target > array[split2]:
            left = split2 + 1
        else:
            left = split1 + 1
            right = split2 - 1

    # If the target is not found, return -1
    return (f'Target "{target}" is not located in the array.')
