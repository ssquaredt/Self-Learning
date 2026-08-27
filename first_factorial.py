def FirstFactorial(num):
    # Question
    # Have the function FirstFactorial (num) take the num parameter being passed and return the factorial of it. 
    # For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. 
    # For the test cases, the range will be between 1 and 18 and the input will always be an integer.

    # Need to ensure the input is integer
    num = int(num)

    # Base case as 0! and 1! = 1, total is the answer of the program
    total = 1
    
    # We must use range() to loop through numbers! Use num + 1 because range() is exclusive of the upper limit
    # If num = 5, without + 1 will result in only loop until 4
    for i in range(1, num + 1):
        # Calculation of num!
        total *= i

    # Answer 
    return total

print(FirstFactorial(input()))
