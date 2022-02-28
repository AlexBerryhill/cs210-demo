import imp
import time
import random
from clown import Clown
from child import Child
from person import Person

def current_time_ms():
    return round(time.time() * 1000)

clown = Clown()
child = Child()
# person = Person()
persons = [Clown(), Person(), Child(), Clown()]

# print(f"The person says, '{person.speak()}'")
# print(f"The clown says, '{clown.speak()}'")
# print(f"The child says, '{child.speak()}'")

for i in range(len(persons)):
    person:Person = persons[i]
    print(f"This one says, '{person.speak()}'")

# print(current_time_ms())

# first_balloon = clown.buy_balloon(3)
# second_balloon = clown.buy_balloon(3)
# balloon_list = []
# for i in range(10):
#     balloon_list.append(clown.buy_balloon(random.randint(1,13)))

# print(clown)

# #while game is running
# first_balloon.update(current_time_ms())
# first_balloon.pop()
# balloon_list[random.randint(0,9)].pop()

# for balloon in balloon_list:
#     print(balloon)
#     #print(f"Long way: {balloon.color}: {balloon.volume_ml}")