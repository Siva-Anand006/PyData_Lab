class SimpleClass:
    
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"
    

class simpleClass2:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def greet(self):
        return f"hello '{self.name}' your roll number is '{self.roll_no}'"
    
class Car:
    def __init__(self, name, model, hp):
        self.name = name
        self.model = model
        self.hp = hp

    def car_info(self):
        return f"Car Name: {self.name}, Model: {self.model}, HP: {self.hp}"
    
    def __add__(self, other):
        return (self.name + other.name)
    
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
            return f"{self.name} says whatever it says!"
    
    def __add__(self, other):
        # Combine names and return a new Animal
        new_name = f"{self.name}-{other.name}"
        return new_name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

        def speak(self):
            return f"{self.name} says Woof!"
        
class cat(Animal):
    def __init__(self,name, breed, sound):
        super().__init__(name)
        self.breed = breed
        self.sound = sound

        def speak(self):
            return f"{self.name} says {self.sound}!"
            
if __name__ == "__main__":
    # Create an instance of SimpleClass
    obj = SimpleClass("World")
    studnet = simpleClass2("Amit", 123)
    # Print the object
    print(obj.greet())
    print(studnet.greet())

#Create an instance of dog
dog = Dog("Tommy", "Pug")
print(dog.speak())

#Create an instance of cat
cat = cat("chichi", "Pug", "Meow")
print(cat.speak())

print(cat + dog)