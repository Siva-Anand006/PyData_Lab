def factorial(n):
    if(n == 0):
        return 1
    else:
        return n*factorial(n-1)

def main():
    try:
        num = int(input("Please enter a number you want to find the factorial of"))
        if(num < 0):
            print("factorial is not defined for a negative number")
        else:
            result = factorial(num)
            print(f"The factorial of {num} is {result}.")
    
    except ValueError:
        print("Please enter a valid integer")

if __name__ == "__main__":
    main()



'''

Factorial Function:
We define a function called factorial that takes an integer n as input 
and returns the factorial of n. This function is implemented using recursion, 
which means it calls itself with a smaller input until it reaches the base case (when n equals 0), at which point it returns 1.

Main Function:
We define a function called main which serves as the entry point of our program.
Inside the main function, we first prompt the user to input a number. 
Then, we check if the number is negative. If it is, we print a message saying that 
factorial is not defined for negative numbers. If it's not negative, we proceed to calculate 
the factorial using the factorial function and display the result.

if __name__ == "__main__":
This line is a Python idiom that checks whether the script is being run 
directly by the Python interpreter (__name__ == "__main__") or if it is being imported into another script.
If the script is being run directly, i.e., 
if it is the main program being executed, then the condition __name__ == "__main__" evaluates to True. 
In this case, Python will execute the code block that follows.
By putting our main() function inside this if block, we ensure that it will only 
be called when the script is run directly, not when it is imported into another script. 
This is a good practice because it allows us to reuse functions defined in this script 
without running the main part of the program every time we import it.

'''