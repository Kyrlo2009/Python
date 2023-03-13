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
        self.money = 1500
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.cheat += 3
        self.progress += 5
        self.gladness -= 5
        self.money -= 40

    def to_sleep(self):
        print("I will sleep")
        self.cheat -= 1
        self.gladness += 3
        self.progress -= 1
        self.money -= 10

    def to_chill(self):
        print("Rest time")
        self.cheat -= 2
        self.gladness += 5
        self.progress -= 3
        self.money -= 70

    def work(self):
        print("Time to work...")
        self.cheat -= 2
        self.gladness -= 3
        self.progress -= 2
        self.money += 200

    def stydyX4(self):
        print("TIME TO STUDY VERY MUCH")
        self.progress += 60
        self.gladness -= 20
        self.money -= 20
        self.end_of_day()

    def cheating(self):
        print("TIME TO CHEATING")
        self.cheat += 50
        self.gladness -= 10
        self.end_of_day()
        self.money -= 20

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
                self.money += 1500
                print(f"Exam = {round(self.progress, 2)}%")
                print(f"Money + 1500")
                print(f"Money = {round(self.money)}")
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
                print(f"Money + 1500")
                print(f"Money = {round(self.money)}")
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
        elif self.money == 0:
            print("Cast out…")
            print("You paid all the money")
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
        print(f"Money = {self.money}")

    def live(self, day):
        day_format = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day_format:=^50}")

        if day != 182:
            if day != 181:
                if day != 364:
                    if day != 365:
                        if self.money <= 150:
                            if self.progress >= -11:
                                if self.gladness >= 5:
                                    self.work()
                                    self.end_of_day()
                                    self.is_alive()
                                    print("Today`s evening...")
        else:
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

        if day == 181:
            self.fate()
        elif day == 364:
            self.fate()
        elif day == 182:
            self.exam()
        elif day == 365:
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