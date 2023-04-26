def info():
    print('-'*40)
    print('''Radix sort has a time complexity of O(d*(n+k)), where d is the number
of digits in the maximum value, n is the size of the input array, and k
is the base of the number system used (which is 10 in this implementation).
Therefore, radix sort can be more efficient than comparison-based sorting
algorithms (such as quicksort or mergesort) when the number of digits in the
input numbers is significantly smaller than the input size n. However, it
requires extra space to store the buckets, which can be a disadvantage when
dealing with large datasets.
''')
    print('-'*40)
def radix_sorting(arr):
    max_digit = max(arr)
    digit_count = 0
    while max_digit > 0:
        digit_count += 1
        max_digit //= 10

    for i in range(digit_count):
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = (num // 10 ** i) % 10
            buckets[digit].append(num)

        arr = []
        for bucket in buckets:
            arr.extend(bucket)

    return arr
