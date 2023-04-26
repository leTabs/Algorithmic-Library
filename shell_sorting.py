def info():
    print('-'*40)
    print('''
Shell sort is an efficient sorting algorithm that builds upon the insertion
sort algorithm. It was invented by Donald Shell in 1959 and is also sometimes
called "diminishing increment sort". The algorithm works by first sorting elements that are far
''')
    print('-'*40)

def shell_sorting(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
    return array
