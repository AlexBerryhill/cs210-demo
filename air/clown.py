from balloon import Balloon
from tank import Tank

class Clown:
    def __init__(self) -> None:
        self.tank = Tank("Helium")
        self.money = 0
        self.balloons = []

    def buy_balloon(self, cost):
        balloon = Balloon("Red")
        balloon.fill(self.tank.release_air(500))
        self.money += cost
        return balloon