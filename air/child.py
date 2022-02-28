from person import Person

class Child(Person):
    def __init__(self) -> None:
        super().__init__()
        self.__has_balloon = False

    def has_balloon(self) -> bool:
        return self.__has_balloon
    
    def speak(self):
        return super().speak()+"\nI want a balloon?"