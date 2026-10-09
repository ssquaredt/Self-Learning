# Question: Bubble Sort
# An array with values to sort.
# An inner loop that goes through the array and swaps values if the first value is higher than the next value. This loop must loop through one less value each time it runs.
# An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n-1 times.

def bubble_sort():
    array = input().split(',')
    n = len(array)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if int(array[j]) > int(array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    
    return array

print(bubble_sort())
