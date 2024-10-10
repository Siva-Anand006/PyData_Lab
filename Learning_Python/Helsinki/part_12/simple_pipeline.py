import csv

def generator(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            yield row
    

    pass