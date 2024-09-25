'''
u are provided with a class named Car that represents a car's features through the following attributes:

make (a string representing the car manufacturer)
top_speed (an integer representing the car's top speed)
You need to implement a function named fastest_car(cars: list) that takes a list
of Car objects as an argument and returns the make of the fastest car.

The function should not modify the input list of Car objects or the Car class definition.
You can assume that there will always be a single car with the highest top speed in the provided list.

'''

class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

def fastest_car(cars: list) -> str:
    fastest = cars[0]
    for car in cars:
        if car.top_speed > fastest.top_speed:
            fastest = car
    return fastest.make
    

if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))  # Output should be "Ferrari"
