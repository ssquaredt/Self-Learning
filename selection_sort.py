# Question: Selection Sort
# An array with values to sort.
# An inner loop that goes through the array and finds the lowest value, keeping track of where it is.
# An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n-1 times.
# Swap the value at the current index with the lowest value found.

def selection_sort():
    array = input().split(',')
    n = len(array)
    
    for i in range(n-1):
        minVal = int(array[i])
        minIdx = i
        
        for j in range(i+1, n):
            if int(array[j]) < minVal:
                minVal = int(array[j])
                minIdx = j
        
        array[i], array[minIdx] = array[minIdx], array[i]
    
    return array

print(selection_sort())