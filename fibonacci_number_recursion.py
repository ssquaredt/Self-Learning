def fibonacci_number_recursion(n):
    # Base case: return n if it is 0 or 1
    if n <= 1:
        return n
    
    # Recursive step: return the sum of the previous two Fibonacci numbers
    else:
        return fibonacci_number_recursion(n-1) + fibonacci_number_recursion(n-2)

print(fibonacci_number_recursion(int(input())))
