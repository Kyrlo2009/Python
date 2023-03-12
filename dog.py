import random


class Dog:
    def __init__(self, name, nation):
        self.hunger = 10
        self.age = 6
        self.nation = nation
        self.irritation = 0
        self.happiness = 10
        self.name = name
        self.alive = True
        self.cube_of_bf = random.randint(1, 5)
        self.cube_of_d = random.randint(1, 5)

    def breakfast(self):
        print("Time to breakfast")
        cube_of_bf = random.randint(1, 5)
        if cube_of_bf == 5:
            print("No\n")
            self.hunger -= 3
            self.irritation += 3
            self.happiness -= 4
        if cube_of_bf < 5:
            print("Hrum-hrum-hrum\n")
            self.hunger += 3
            self.happiness += 1

    def play(self):
        print("Time to play")
        print("Hi")
        print(f"I am " + self.name + ". I am " + self.nation + "\n")
        self.irritation -= 1
        self.happiness += 2
        self.hunger -= 4

    def sleep(self):
        print("Time to slee...\nZ-z-z\n")
        self.hunger -= 2
        self.irritation -= 2
        self.happiness += 2

    def dinner(self):
        print("Time to dinner")
        print("Hrum-hrum-hrum\n")
        cube_of_d = random.randint(1, 5)
        if cube_of_d == 5:
            self.hunger -= 3
            self.irritation += 5
            self.happiness -= 5
        if cube_of_d < 5:
            self.hunger += 3
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
        self.breakfast()
        if live_cube == 1:
            self.play()
        elif live_cube == 2:
            self.sleep()
        self.dinner()
        self.end_of_day()
        self.is_alive()

rich = Dog(name="Richard", nation="Chihuahua")
for day in range(365):
    if rich.alive == False:
        break
    rich.live(day+1)