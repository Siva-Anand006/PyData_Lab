import sys

def fibonacci_list(limit):
    fib_sequence = [0, 1]
    while len(fib_sequence) < limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Generating the first 10 Fibonacci numbers
fib_numbers1 = fibonacci_list(10)

print(fib_numbers1)

def fibonacci_generator():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a+b
         

# Using the generator to get the first 10 Fibonacci numbers
fib_gen = fibonacci_generator()
fib_numbers = [next(fib_gen) for _ in range(10)]
print(fib_numbers)

