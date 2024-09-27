class Player:
    def __init__(self, name: str, goals: int):
        self.name = name
        self.goals = goals
        
    def __str__(self) -> str:
        print(f"{self.name} : {self.goals}")
        

class Team:
    def __init__(self, name) -> None:
        self.name = name
        self.players = []
        
    def add_player(self,player: Player ):
        self.players.append(player)
    
    def summary(self):
        goal_list = [member.goals for member in self.players]
        
        print(f"Team : {self.name}")
        print(f"Players : {len(self.players)}")
        print(f"Goals scored by each player : {goal_list}")

        
if __name__ == "__main__":
    
    ca = Team("Campus Allstars")
    ca.add_player(Player("Eric", 10))
    ca.add_player(Player("Emily", 22))
    ca.add_player(Player("Andy", 1))
    ca.summary()
