class Computer:
    def __init__(self, model : str, speed : int) -> None:
        self.model = model
        self.speed = speed
    
    def __str__(self) -> str:
        return f"{self.model}, {self.speed}"    

class LaptopComputer(Computer):
    def __init__(self, model: str, speed: int, weight : int) -> None:
        super().__init__(model, speed)
        self.weight = weight
    
    def __str__(self) -> str:
        return f"{self.model}, {self.speed}, {self.weight} kg"
    
class ComputerGame:
    def __init__(self, name, company, year : int) -> None:
        self.name = name
        self.company  = company
        self.year = year
    pass

class GameWarehouse:
    def __init__(self) -> None:
        self.games = []
    
    def addgame(self, game : ComputerGame):
        self.games.append(game)
        
    def list_games(self):
        return self.games

class GameMuseum(GameWarehouse):
    def __init__(self) -> None:
        super().__init__(self.games)
        
    def list_games(self):
        for game in super().list_games():
            if game.year > 1990:
                return self.games 


if __name__ == "__main__":
    
    laptop = LaptopComputer("Asus Flipbook", 1250, 2)
    print(laptop)
    
