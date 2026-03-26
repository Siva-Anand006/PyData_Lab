def count(number):
    while number > 0:
        yield number
        number -= 1

if __name__ == "__main__":
    print("hello world")

    try:
        result = 10 / 1  # This will raise an error
        print("code was run")
    except ZeroDivisionError:
        print("Oops! Can't divide by zero.")
# Output: Oops! Can't divide by zero.

for x in count(3):
    print(x)

list1 = [ x  for x in count(3)]

for item in list1:
    print(item)