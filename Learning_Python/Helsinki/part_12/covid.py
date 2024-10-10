import csv

def covid_data_generator(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            yield row


def count_lines(filename):
   case_generator = covid_data_generator(filename)
   counter = 0
   for _ in case_generator:
       counter +=1
   return counter
    

# count cases by country

def count_cases_in_country(filename, country):
    case_generator = covid_data_generator(filename)
    total_cases = 0
    for row in case_generator:
        if row[2] == country:  # Assuming the country column is at index 2
            total_cases += int(row[3])  # Assuming the case count is at index 3
    return total_cases

filename = "Datasets\Covid_19_Dataset.csv"
country = "Argentina"
total_cases = count_cases_in_country(filename, country)
print(f"Total COVID-19 cases in {country}: {total_cases}")
print(f"Total number of lines in the file is {count_lines(filename)}")