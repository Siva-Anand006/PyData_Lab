'''Implementing a Car Class with Encapsulation and Methods
Task:

Please implement a class named Car with two private, encapsulated variables:

petrol: the amount of petrol in the tank, which ranges from 0 to 60 litres.
odometer: the odometer reading, representing the distance driven in kilometres.
The car should consume one litre of petrol per kilometre driven.

Requirements:

The class should contain the following methods:

fill_up():

Fills the petrol tank to its maximum capacity (60 litres).


drive(km: int):
Drives the car for the specified distance (km), or as far as the available petrol allows.
For each kilometre driven, reduce the petrol by one litre.
Update the odometer based on the actual distance driven.
__str__():

Returns a string representation of the car's current state in the format:
arduino
Copy code
"Odometer: x km, Petrol: y litres"
where x is the total kilometres driven and y is the remaining petrol in the tank.'''

class Car:
    
    def __init__(self ) -> None:
        self.__petrol = 0
        self.__odometer = 0
        
    def fill_up(self):
        self.__petrol = 60

    
    def drive(self, km: int):
        if self.__petrol >= km:
           self.__petrol -= km
           self.__odometer += km
        else:
           self.__odometer += self.__petrol
           self.__petrol = 0
           print("Insufficient fuel to continue journey.")
    
    def __str__(self) -> str:
        return (f"Odometer: {self.__odometer} km, Petrol: y litres : {self.__petrol}")
    

if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)
