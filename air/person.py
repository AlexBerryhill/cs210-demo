from wallet import Wallet

class Person:
    def __init__(self) -> None:
        self._wallet = Wallet(0)

    def __str__(self) -> str:
        return "(person)"
        
    # def get_wallet(self):
    #     return self._wallet