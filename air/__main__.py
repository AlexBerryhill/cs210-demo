import time
import random
from clown import Clown

def current_time_ms():
    return round(time.time() * 1000)

clown = Clown()

print(current_time_ms())

first_balloon = clown.buy_balloon(3)
second_balloon = clown.buy_balloon(3)
balloon_list = []
for i in range(10):
    balloon_list.append(clown.buy_balloon(random.randint(1,13)))

#while game is running
first_balloon.update(current_time_ms())
first_balloon.pop()
balloon_list[random.randint(0,9)].pop()

for balloon in balloon_list:
    print(balloon)
    #print(f"Long way: {balloon.color}: {balloon.volume_ml}")