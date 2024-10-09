def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

# Get the first 10 prime numbers
print(generate_primes(10))


def prime_generator():
    num = 2  # Start with the first prime number
    while True:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # Check for factors up to the square root of num
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

# Using the generator to get the first 10 prime numbers
prime_gen = prime_generator()
primes = [next(prime_gen) for _ in range(10)]
print(primes)
