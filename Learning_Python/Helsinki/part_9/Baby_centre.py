'''
### Programming Exercise

#### Exercise: Implement the `BabyCentre` Class

The exercise template contains a class named `Person` and a partially implemented class `BabyCentre`. The `BabyCentre` class should be able to perform various actions on a `Person` object, such as weighing and feeding them. Your task is to complete the `BabyCentre` class by implementing three methods: `weigh`, `feed`, and `weigh_ins`.

**Instructions:**

1. **Weighing Persons:**
   - Implement the method `weigh(self, person: Person)` in the `BabyCentre` class.
   - This method should take a `Person` object as an argument and return the weight of that person.
   - You can access the weight of the person through the appropriate attribute defined in the `Person` class.

   Example usage:
   ```python
   baby_centre = BabyCentre()

   eric = Person("Eric", 1, 110, 7)
   peter = Person("Peter", 33, 176, 85)

   print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
   print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")
   ```
   Expected output:
   ```
   Eric weighs 7 kg
   Peter weighs 85 kg
   ```

2. **Feeding Persons:**
   - Implement the method `feed(self, person: Person)` in the `BabyCentre` class.
   - This method should increase the weight of the `Person` object passed as an argument by one.

   Example usage:
   ```python
   baby_centre = BabyCentre()

   eric = Person("Eric", 1, 110, 7)
   peter = Person("Peter", 33, 176, 85)

   print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
   print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")
   print() 

   baby_centre.feed(eric)
   baby_centre.feed(eric)
   baby_centre.feed(eric)

   print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
   print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")
   ```
   Expected output:
   ```
   Eric weighs 7 kg
   Peter weighs 85 kg

   Eric weighs 10 kg
   Peter weighs 85 kg
   ```

3. **Counting Weigh-Ins:**
   - Implement the method `weigh_ins(self)` in the `BabyCentre` class.
   - This method should return the total number of times any person has been weighed using the `BabyCentre` object.
   - You will need to maintain a counter as a new attribute in the `BabyCentre` class to keep track of the number of weigh-ins.

   Example usage:
   ```python
   baby_centre = BabyCentre()

   eric = Person("Eric", 1, 110, 7)
   peter = Person("Peter", 33, 176, 85)

   print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

   baby_centre.weigh(eric)
   baby_centre.weigh(eric)

   print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

   baby_centre.weigh(eric)
   baby_centre.weigh(eric)
   baby_centre.weigh(eric)
   baby_centre.weigh(eric)

   print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")
   ```
   Expected output:
   ```
   Total number of weigh-ins is 0
   Total number of weigh-ins is 2
   Total number of weigh-ins is 6
   ```

### Summary

- Implement the `weigh` method to return the weight of a `Person` object.
- Implement the `feed` method to increase the weight of a `Person` object by 1.
- Implement the `weigh_ins` method to track how many times the `BabyCentre` object has performed weigh-ins.

Make sure to test your implementation thoroughly using the examples provided.

'''

class Person:
    def __init__(self, name: str,age : int, height : int, weight: int):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

class Babycentre: 

    def __init__(self):
        self.weigh_in = 0
    
    def weigh(self, person: Person):
        # return the weight of the person passed as an argument
        self.weigh_in +=1 
        return person.weight
    
    def feed(self,person :Person):
        person.weight +=  1
        
    def weigh_ins(self):
        return self.weigh_in


if __name__ == "__main__":
    baby_centre = Babycentre()

    eric = Person("Eric", 1, 110, 7)
    peter = Person("Peter", 33, 176, 85)

    print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
    print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")
    
    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")
    
    baby_centre.feed(eric)
    baby_centre.feed(eric)
    baby_centre.feed(eric)

    print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
    print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")
    
    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

    baby_centre.weigh(eric)
    baby_centre.weigh(eric)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

    baby_centre.weigh(eric)
    baby_centre.weigh(eric)
    baby_centre.weigh(eric)
    baby_centre.weigh(eric)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")