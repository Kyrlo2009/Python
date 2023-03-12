import random


class Dog:
    def __init__(self, years, nat_of_dog, name=None):
        self.hunger = 10
        self.age = years
        self.nation = nat_of_dog
        self.irritation = 0
        self.happiness = 10
        self.name = name
        self.alive = True

    def breakfast(self, cube_of_bf):
        print("Time to breakfast")
        cube_of_bf = random.randint(1, 6)
        if cube_of_bf == 10:
            self.hunger -= 2
            self.irritation += 3
            self.happiness -= 2
        if cube_of_bf >= 10:
            self.hunger += 2
            self.happiness += 1

    def play(self):
        print("Time to play")
        print("Hi")
        print(f"I am {round(self.nation)}")
        self.irritation -= 1
        self.happiness += 1
        self.hunger -= 3

    def sleep(self):
        print("Time to slee...\nZ-z-z")
        self.hunger -= 2
        self.irritation -= 1
        self.happiness += 2

    def dinner(self, cube_of_d):
        print("Time to dinner")
        cube_of_d = random.randint(1, 6)
        if cube_of_d == 10:
            self.hunger -= 2
            self.irritation += 2
            self.happiness -= 2
        if cube_of_d >= 10:
            self.hunger += 2
            self.happiness += 1

    def is_alive(self):
        if self.hunger <= 0:
            print("Died of hunger")
            self.alive = False
        elif self.happiness <= 0:
            print("Depression… Coming from home")
            self.alive = False
        elif self.irritation >= 10:
            print("Bit...In a shelter now...")
            self.alive = False

    def end_of_day(self):
        print(f"Hunger = {self.hunger}")
        print(f"Irritation = {self.irritation}")
        print(f"Happiness = {round(self.happiness)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")

        if self.hunger <= 3:
            if self.happiness >= 3:
                self.breakfast()
        if self.happiness <= 3:
            if self.hunger >= 4:
                self.play()

        live_cube = random.randint(1, 2)
        if live_cube == 1:
            self.play()
        elif live_cube == 2:
            self.sleep()
        self.end_of_day()
        self.is_alive()

richard = Dog(name="Richard", nat_of_dog="Chihuahua", years=6)
for day in range(365):
    if richard.alive == False:
        break
    richard.live(day+1)