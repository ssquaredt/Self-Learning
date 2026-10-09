# Question: Fibonacci Number in Loops
# What the code need to have:
# 1. Two variables to hold the previous two Fibonacci numbers
# 2. For loop that runs for a specific count (user input)
# 3. Create new Fibonacci numbers by adding two previous ones
# 4. Print the new Fibonacci number
# 5. Update the variables that hold the previous two fibonacci numbers

def fibonacci_number_loop(num):
    prev1 = 0
    prev2 = 1
    
    print(prev1)
    print(prev2)

    for i in range(num):
        new_fib = prev1 + prev2
        print(new_fib)
        prev1 = prev2
        prev2 = new_fib 

fibonacci_number_loop(int(input()))