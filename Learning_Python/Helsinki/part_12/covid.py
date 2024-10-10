import csv

def covid_data_generator(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            yield row

# count cases by country

def count_cases_in_country(filename, country):
    case_generator = covid_data_generator(filename)
    total_cases = 0
    for row in case_generator:
        if row[2] == country:  # Assuming the country column is at index 1
            total_cases += int(row[3])  # Assuming the case count is at index 3
    return total_cases

filename = "Datasets\Covid_19_Dataset.csv"
country = "Argentina"
total_cases = count_cases_in_country(filename, country)
print(f"Total COVID-19 cases in {country}: {total_cases}")
