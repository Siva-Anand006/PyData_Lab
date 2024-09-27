class Vehicle:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
    
    def info(self):
        return f"Make: {self.make}, Model: {self.model}, Year:{self.year}"
    
class Car(Vehicle):
    def __init__(self,make, model, year,fuel_type) -> None:
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        
    def info(self):
        return f"Make: {self.make}, Model: {self.model}, Year:{self.year}, Fuel Type: {self.fuel_type}"
    
if __name__ == "__main__":
    
    # Create a Vehicle object
    vehicle = Vehicle("Toyota", "Corolla", 2015)
    print(vehicle.info())  # Output: Make: Toyota, Model: Corolla, Year: 2015

    # Create a Car object
    car = Car("Honda", "Civic", 2020, "Petrol")
    print(car.info())  # Output: Make: Honda, Model: Civic, Year: 2020, Fuel Type: Petrol
