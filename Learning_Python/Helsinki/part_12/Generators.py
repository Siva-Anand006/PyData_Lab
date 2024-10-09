def count_up_to(n):
    count = 1
    while count < n:
        yield count
        count += 1
        
counter = count_up_to(5)

for item in counter:
    print(item)
    
import sys

# Creating a list of numbers from 1 to 1,000,000
numbers_list = [x for x in range(1, 1000001)]
print("Size of list:", sys.getsizeof(numbers_list), "bytes")

# Creating a generator of numbers from 1 to 1,000,000
numbers_generator = (x for x in range(1, 1000001))
print("Size of generator:", sys.getsizeof(numbers_generator), "bytes")

print(numbers_generator)


import time

# Using a list comprehension
start_time = time.time()
numbers_list = [x for x in range(1, 1000001)]
list_sum = sum(numbers_list)
list_time = time.time() - start_time
print("List sum:", list_sum)
print("Time taken with list:", list_time, "seconds")
print("Size of list:", sys.getsizeof(numbers_list), "bytes")

# Using a generator expression
start_time = time.time()
numbers_generator = (x for x in range(1, 1000001))
generator_sum = sum(numbers_generator)
generator_time = time.time() - start_time
print("Generator sum:", generator_sum)
print("Time taken with generator:", generator_time, "seconds")
print("Size of generator:", sys.getsizeof(numbers_generator), "bytes")

