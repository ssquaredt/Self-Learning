# Question: Find The Lowest Value in an Array
# Create an array to hold the user input
# Create a variable minVal and set it equal to the first value of the array
# Loop to go through every element in the array
# Compare the current element with minVal, update minVal if the current element is smaller
# Return minVal after looking at all the elements

def lowest_value_in_array():
    array = input().split(",")
    minVal = int(array[0])

    for i in array:
        if int(i) < minVal:
            minVal = int(i)
            
    return minVal

print(lowest_value_in_array())