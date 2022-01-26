import time
import random
from balloon import Balloon

def current_time_ms():
    return round(time.time() * 1000)

print(current_time_ms())
first_balloon = Balloon("Red")
second_balloon = Balloon("Blue")
balloon_list = []
for i in range(10):
    balloon_list.append(Balloon("Green"))

#while game is running
first_balloon.update(current_time_ms())
first_balloon.pop()
balloon_list[random.randint(0,9)].pop()

for balloon in balloon_list:
    print(balloon)
    #print(f"Long way: {balloon.color}: {balloon.volume_ml}")