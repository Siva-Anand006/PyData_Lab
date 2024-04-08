#Random password generator in python
import string
import random
    
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password
    
def main():
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Password length should be greater than zero.")
        else:
            password = generate_password(length)
            print("Generated Password:", password)
        
    except ValueError:
        print("Enter a valid integer.")
    

if __name__ == "__main__":   # why we running this?
    main()

