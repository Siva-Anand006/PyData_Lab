"""products = [
    ("banana", 5.95, 12),
    ("apple", 3.95, 3),
    ("orange", 4.50, 2),
    ("watermelon", 4.95, 22),
    ("kale", 0.99, 1)
]

def search(products: list, criterion: callable):
    return [ product for product in products if criterion(product) ]

def price_under_4_euros(product : tuple):
    if product[1] < 4 : 
        return product[1]  

# Usage
filtered_products = search(products, price_under_4_euros)
print(filtered_products)  # Output: [('apple', 3.95, 3), ('kale', 0.99, 1)]


#print(price_under_4_euros(products))"""


products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22), ("kale", 0.99, 1)]

def filter_by_stock(products : list, criterion : callable):
    return [ product for product in products if criterion(product) ]

def stock_above_5(product : tuple):
    return product[2] > 5


    

filtered_products = filter_by_stock(products, stock_above_5)
print(filtered_products)