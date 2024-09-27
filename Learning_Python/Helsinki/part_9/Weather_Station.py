'''
Implementing a WeatherStation Class with Encapsulation
Task:

Create a class named WeatherStation that is used to store observations about the weather. The class should meet the following requirements:

Requirements:
class WeatherStation
add_observation(observation: str):
latest_observation():
number_of_observations() 
Constructor:
Takes the name of the station as an argument.
__str__()

Methods:

add_observation(observation: str): Adds an observation as the last entry in a list.
latest_observation(): Returns the latest observation added to the list. If there are no observations yet, this method should return an empty string.
number_of_observations(): Returns the total number of observations added.
__str__(): Returns a string representation of the station name and the total number of observations as shown in the example below.

'''

class WeatherStation:
    def __init__(self, name : str) -> None:
        self.name = name
        self.observations = []
    
    def add_observation(self,observation: str):
        self.observations.append(observation)
    
    def latest_observation(self):
        return self.observations[-1] 
    
    def number_of_observations(self) :
        self.Count_observations = len(self.observations)
        return self.Count_observations
    
    def __str__(self) -> str:
        return f"Station {self.name} has {self.Count_observations} observations"

if __name__ == "__main__":
    
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    
    station.add_observation("Sunny")
    print(station.latest_observation())  # Output: Sunny

    station.add_observation("Thunderstorm")
    print(station.latest_observation())  # Output: Thunderstorm

    print(station.number_of_observations())  # Output: 3
    print(station)  # Output: Station Houston has 3 observations
