
def orderby(n:tuple):
    return n[1]

def sort_by_price(items: list):
    return sorted(items, key= orderby)


groceries = [
    ("Apples", 3.99),
    ("Bananas", 1.29),
    ("Milk", 4.49),
    ("Bread", 2.99),
    ("Eggs", 5.59),
    ("Cheese", 7.99),
    ("Tomatoes", 2.49),
    ("Chicken Breast", 9.99),
    ("Rice", 4.79),
    ("Pasta", 3.49)
]

products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22), ("kale", 0.99, 1)]

groceries.sort(key= orderby) 
#The sort() method will automatically call the orderby() function on each element of the list to determine the sort order.

print(groceries)

reversed_groceries = sorted(groceries, key= orderby, reverse= True)
print(reversed_groceries)

for grocery in sort_by_price(groceries):
    print(grocery)

#To get the reversed sorted list, you should use the sorted() function, which returns a new sorted list, instead of modifying the original list in place. 