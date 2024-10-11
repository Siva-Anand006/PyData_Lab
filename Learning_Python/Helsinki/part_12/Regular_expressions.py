import re

#Problem 1: Validate Email Address
#*Task**: Write a regex pattern to validate email addresses.

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Test the function
print(validate_email("example@test.com"))  # True
print(validate_email("invalid-email.com"))  # False


#Problem 2: Extract Phone Numbers
#**Task**: Extract all phone numbers from a given string.

def extract_phone_numbers(text):
    pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
    return re.findall(pattern, text)

# Test the function
sample_text = "Contact us at 123-456-7890 or 987.654.3210."
print(extract_phone_numbers(sample_text))  # ['123-456-7890', '987.654.3210']


#Problem 3: Find All Dates
#**Task**: Find all dates in the format "dd-mm-yyyy" from a given string.

def find_dates(text):
    pattern = r'\b\d{2}-\d{2}-\d{4}\b'
    return re.findall(pattern, text)

# Test the function
sample_text = "Important dates are 01-01-2020 and 15-03-2021."
print(find_dates(sample_text))  # ['01-01-2020', '15-03-2021']

#Problem 4: Replace Multiple Spaces
#**Task**: Replace multiple consecutive spaces with a single space in a string.

def replace_multiple_spaces(text):
    pattern = r'\s+'
    return re.sub(pattern, ' ', text)

# Test the function
sample_text = "This    is   a    test."
print(replace_multiple_spaces(sample_text))  # "This is a test."

#Problem 5: Check for Hexadecimal Color Code
#*Task**: Write a regex pattern to check if a string is a valid hexadecimal color code.

def is_valid_hex_color(color):
    pattern = r'^#(?:[0-9a-fA-F]{3}){1,2}$'
    return bool(re.match(pattern, color))

# Test the function
print(is_valid_hex_color("#1A2B3C"))  # True
print(is_valid_hex_color("#XYZ123"))  # False

