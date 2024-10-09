
class ClimbingRoute:
    def __init__(self, name : str, length : int, grade: str) -> None:
        self.name = name
        self.length = length
        self.grade = grade
        
    def __str__(self) -> str:
        return f"{self.name}, length {self.length} metres, grade {self.grade}"
        
def access_length(n : ClimbingRoute):
    return n.length

def sort_by_length(routes : list):
    return sorted(routes, key = access_length, reverse=True)

def sort_by_length1(routes : list):
    return sorted(routes, key = lambda x : x. length if x is ClimbingRoute else 0, reverse= True)


route1 = ClimbingRoute("Edge", 38, "6A+")
route2 = ClimbingRoute("Smooth operator", 11, "7A")
route3 = ClimbingRoute("Synchro", 14, "8C+")

#part1
print(route1)
print(route2)
print(route3.name, route3.length, route3.grade)

#part2
r1 = ClimbingRoute("Edge", 38, "6A+")
r2 = ClimbingRoute("Smooth operator", 11, "7A")
r3 = ClimbingRoute("Synchro", 14, "8C+")
r4 = ClimbingRoute("Small steps", 12, "6A+")

routes = [r1, r2, r3, r4]
print("sorted routes")

for route in sort_by_length1(routes):
    print(route)
