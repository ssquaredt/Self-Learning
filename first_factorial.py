"""
Question: First Factorial
- Have the function FirstFactorial (num) take the num parameter being passed
and return the factorial of it.

- For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24

Example workflow:
- if num = 4
return 4 * first_factorial(3) # 4-1 = 3

- if num = 3
return 3 * first_factorial(2)

- if num = 2
return 2 * first_factorial(1)

first_factorial(1) = 1

first_factorial(2) = 2 * first_factorial(1)
                   = 2 * 1
                   = 2

first_factorial(3) = 3 * first_factorial(2)
                   = 3 * 2
                   = 6

first_factorial(4) = 4 * first_factorial(3)
                   = 4 * 6
                   = 24
"""


def first_factorial(num):
    # try except block to handle Value Error (non-integer like string)
    try:
        # Initialize user input to integer
        num = int(num)
        # Base Case
        if num == 1:
            return 1
        # Recursion, minus the number of n and call the function again when
        # n > 1 to reach the base case
        elif num > 1:
            return num * first_factorial(num - 1)
        # Error handling if user input is negative number
        else:
            return "Wrong input. Please insert a positive number."

    except ValueError:
        return "Wrong input. Please insert a positive number"


user_input = input(
    "Please insert a positive number to calculate its factorial: "
)


print(first_factorial(user_input))
