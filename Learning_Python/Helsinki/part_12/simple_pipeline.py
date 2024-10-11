# Modified generator function to return both column names and row data

import csv
def generator(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        cols = next(reader)  # Extract column names
        for row in reader:
            yield cols, row  # Yield both column names and the row data

# Use a generator comprehension to create dictionaries with column names as keys
filename = 'Datasets/techcrunch.csv'
row_generator = generator(filename)

# Create the dictionary generator using the cols from the generator itself
dict_generator = (dict(zip(cols, row)) for cols,row in row_generator)

funding = ( int(company_dict["raisedAmt"]) for company_dict in dict_generator if company_dict["round"] == "a" )

total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")
