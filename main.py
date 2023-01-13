import random
import time

class Kalibr: #Cruise Missile (Parent)
    def __init__(self):
        self._speed = 0

    def random_speed(self):
        self._speed = random.radint(1800, 2200)
        return self._speed
    

    pass

class Kh101(Kalibr): #Cruise Missile of a different type (Child)
    def random_speed(self):
        self._speed = random.randint(200, 600)
        return self._speed
    pass

class Patriot: #Air-Defense System
    def active(self):
        print("The Air-Defense System has been activated:")

class City: #City has HP
    health = 100

def count_down():
    print("The game will begin in:")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(3)
    print("GO!")

def sleep_print(text: str, sec: int):
    print(text)
    time.sleep(sec)

game_started = False

print("Hello, this is a simple text-based Air-Defense simulation.\n")

while True:
    start = input("To start the game type 'Start'...\n").lower()
    if start == "start":
        game_started = True
        break
    else:
        print("You've typed something wrong...")

if game_started:
    city_name = input("What the name of you're city ? ")
    sleep_print("The city {} is under attack from cruise missiles!\nYou are in charge of Air-Defense system.".format(city_name), 3)
    sleep_print("There are 2 types of missiles in the game Kalibr and Kh101, \nKalibr are much faster and harder to hit, but they are more rare.\n", 5)
    sleep_print("The game is purely random and you are just the suspector (Wait for more updates...) so just enjoy the show!\n", 3)
    count_down()
    
