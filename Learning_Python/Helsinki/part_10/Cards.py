class Product:
    def __init__(self, name : str , price : float) -> None:
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

class BonusCard:
    def __init__(self) -> None:
        self.products_brought = []
        
    def add_product(self, product: Product):
        self.products_brought.append(product)

    def calculate_bonus(self) -> float:
        total = sum(item.price for item in self.products_brought)
        return total * 0.05

    def __str__(self) -> str:
        products_list = "\n".join(str(product) for product in self.products_brought)
        return f"BonusCard with products:\n{products_list}"  
        
class PlatinumCard(BonusCard):
    def __init__(self) -> None:
        super().__init__()
    
    def calculate_bonus(self):
        return super().calculate_bonus() * 1.05
    

if __name__ == "__main__":
    card = BonusCard()
    card.add_product(Product("Bananas", 6.50))
    card.add_product(Product("Satsumas", 7.95))
    bonus = card.calculate_bonus()  # Should be 0.72 (5% of 14.45)
    
    card2 = PlatinumCard()
    card2.add_product(Product("Bananas", 6.50))
    card2.add_product(Product("Satsumas", 7.95))
    bonus2 = card2.calculate_bonus()  # Should be 0.756 (additional 5% on top of the basic bonus)
    print(card)
    print(bonus)    # Output: 0.7225
    print(bonus2)   # Output: 0.758625



'''
Implementing Inheritance with Product and BonusCard Classes
Objective:

Create a system that models a bonus card system where customers earn bonuses based on their purchases. You will practice using inheritance by creating a BonusCard class and a PlatinumCard class, which has an additional bonus calculation.

Requirements:

Implement a class named Product that has the following attributes:

name: the name of the product (string)
price: the price of the product (float)
Implement a class named BonusCard that:

Has an attribute products_bought, which is an empty list to store Product objects.
Includes a method add_product(product: Product) that adds the product to products_bought.
Contains a method calculate_bonus() that calculates the bonus as 5% of the total price of all products in products_bought.
Implement a subclass named PlatinumCard that inherits from BonusCard:

In its __init__ method, ensure that it correctly calls the parent class's __init__ method.
Override the calculate_bonus() method to first calculate the bonus using super().calculate_bonus() and then increase the bonus by an additional 5%.

'''