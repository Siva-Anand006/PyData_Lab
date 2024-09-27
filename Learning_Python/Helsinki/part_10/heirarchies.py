# Parent Class
class Animal:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def speak(self):
        return "Some sound"

# Child Class
class Dog(Animal): #parent class in specified in the parentheses
    def __init__(self, name, age, breed):
        super().__init__(name,age)  # Using super() to call the parent class's constructor
        self.breed = breed

    # Overriding the speak method
    def speak(self):
        return "Woof!"

# Using the classes
my_pet = Animal("Kat",2)
print(my_pet.name)
print(my_pet.speak())
my_dog = Dog("Buddy", 4, "Golden Retriever")
print(my_dog.name)
print(my_dog.age)
print(my_dog.breed)
print(my_dog.speak())  # Output: Woof!
