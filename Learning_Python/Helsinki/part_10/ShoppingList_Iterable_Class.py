class ShoppingList:
    def __init__(self):
        self.items = []

    def add(self, product: str, quantity: int):
        self.items.append((product, quantity)) #tuple gets added to a list

    # Implement the __iter__() method here
    def __iter__(self):
        self.n = 0
        return self
    
    # Implement the __next__() method here
    def __next__(self):
        if self.n < len(self.items):
            item = self.items[self.n]
            self.n += 1
            return item
        else:
            raise StopIteration
    

# Test the class
shopping_list = ShoppingList()
shopping_list.add("bananas", 10)
shopping_list.add("apples", 5)
shopping_list.add("pineapple", 1)

for product in shopping_list:
    print(f"{product[0]}: {product[1]} units")
