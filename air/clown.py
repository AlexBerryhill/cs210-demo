from person import Person
from balloon import Balloon
from air_tank import AirTank
from wallet import Wallet


class Clown(Person):
    def __init__(self) -> None:
        self.__tank = AirTank("Helium")

    def buy_balloon(self, cost) -> Balloon:
        balloon = Balloon("Red")
        balloon.fill(self.__tank.release_air(500))
        super()._wallet.add_transaction(cost)
        return balloon

    def __str__(self) -> str:
        return f"Clown ($ {super()._wallet.get_balance():.2f})"