"""
freeCodeCamp Daily Coding Challenge (25.11.2026)

Question: FizzBuzz
- Given an integer (n), return an array of integers from 1 to n (inclusive),
  replacing numbers that are multiple of:
  1) 3 with "Fizz".
  2) 5 with "Buzz".
  3) 3 and 5 with "FizzBuzz".
"""


def fizz_buzz(n):
    # List to store result
    result = []

    # Loop through number from 1 to n where n is user input
    # range(1, n + 1) means starts from 1 to n
    for number in range(1, n + 1):
        # Replace multiple of 3 and 5 with "FizzBuzz"
        if number % 3 == 0 and number % 5 == 0:
            result.append("FizzBuzz")
        # Replace multiple of 3 with "Fizz"
        elif number % 3 == 0:
            result.append("Fizz")
        # Replace multiple of 5 with "Buzz"
        elif number % 5 == 0:
            result.append("Buzz")
        else:
            result.append(number)

    return result


print(fizz_buzz(50))
