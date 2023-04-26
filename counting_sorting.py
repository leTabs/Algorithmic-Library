def info():
    print('-'*40)
    print('''
In the given implementation, the function takes an input list "arr",
finds the maximum value in the list, creates a counting list "count"
with the length of the maximum value + 1, and increments the count of
each element in the input list by 1. Then, the function iterates through
the counting list and inserts the elements into the output list "arr" based
on their count. Finally, the sorted list "arr" is returned.
''')
    print('-'*40)

def counting_sorting(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)
    for num in arr:
        count[num] += 1
    index = 0
    for i in range(max_value + 1):
        for j in range(count[i]):
            arr[index] = i
            index += 1
    return arr
