import random

class Student:
    def __init__(self, name):
        self.name = name
        self.cheat = 30
        self.gladness = 50
        self.progress = 0
        self.cube_of_fate = 1
        self.ticher = random.randint(1, 3)
        self.yesN = random.randint(1, 2)
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.cheat += 3
        self.progress += 5
        self.gladness -= 5

    def to_sleep(self):
        print("I will sleep")
        self.cheat -= 1
        self.gladness += 3
        self.progress -= 2

    def to_chill(self):
        print("Rest time")
        self.cheat -= 2
        self.gladness += 5
        self.progress -= 5


    def stydyX4(self):
        print("TIME TO STUDY VERY MUCH")
        self.progress += 60
        self.gladness -= 20
        self.end_of_day()

    def cheating(self):
        print("TIME TO CHEATING")
        self.cheat += 50
        self.gladness -= 10
        self.end_of_day()

    def fate(self):
        cube_of_fate = random.randint(1, 2)
        if cube_of_fate == 1:
            self.stydyX4()
        if cube_of_fate == 2:
            self.cheating()

    def exam(self):
        self.ticher = random.randint(1, 3)
        print("Time pass exam")
        if self.cube_of_fate == 1:
            if self.progress >= 70:
                print("You pass the exam!")
                print(f"Exam = {round(self.progress, 2)}%")
            elif self.progress < 70:
                print("Cast out…")
                if self.progress <= 0:
                    print(f"Exam = 0%")
                    self.alive = False
                if self.progress > 0:
                    print(f"Exam = {round(self.progress, 2)}%")
                    self.alive = False
        if self.cube_of_fate == 2:
            if self.cheat >= 70:
                print(f"Exam = {round(self.cheat, 2)}%")
            elif self.cheat < 70:
                if self.cheat > 30:
                    print("Cast out…")
                    if self.cheat <= 0:
                        print(f"Exam = 0%")
                        self.alive = False
                    if self.cheat > 0:
                        print(f"Exam = {round(self.cheat, 2)}%")
                        self.alive = False
            elif self.ticher == 5:
                print("Cheating of exam")
                print("Cast out…")
                self.alive = False
            elif self.cheat <= 30:
                print("Cheating of exam")
                print("Cast out…")
                self.alive = False

    def is_alive(self):
        if self.progress < -15:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 150:
            print("Passed externally…")
            self.alive = False

    def end_of_day(self):
        print(f"Cheating = {self.cheat}")
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")

        if self.progress <= -5:
            if self.gladness >= 5:
                self.yesN = random.randint(1, 2)
                if self.yesN == 1:
                    self.to_study()
                if self.yesN == 2:
                    pass
        if self.gladness <= 5:
            if self.progress >= 5:
                self.yesN = random.randint(1, 2)
                if self.yesN == 1:
                    self.to_chill()
                if self.yesN == 2:
                    pass

        if str(day) == "Day " + str(181) + " of " + self.name + " life":
            self.fate()
        elif str(day) == "Day " + str(364) + " of " + self.name + " life":
            self.fate()
        elif str(day) == "Day " + str(182) + " of " + self.name + " life":
            self.exam()
        elif str(day) == "Day " + str(365) + " of " + self.name + " life":
            self.exam()
        else:
            live_cube = random.randint(1, 3)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()
            self.end_of_day()
            self.is_alive()


nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day+1)