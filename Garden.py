import random
import time

from Plant import Plant, Plant_base
import json


def get_plant_from_file(file_name)->list[dict]:
    with open(file_name) as f:
        d = json.load(f)
        f.close()
        return d



class Garden():
    def __init__(self):
        self.name = ""
        self.plants = []
        self.time = 0

    def __str__(self):
        return f"{self.name}{self.plants}{self.time}"

    def add_plant(self):
        choise = input("what plant do you want to add?\n""1:berries\n""2:rose\n""3:apricot\n")
        while choise.isnumeric() or not int(choise) in range(1, 4) :
            print("wrong input")
            choise = input("what plant do you want to add?\n""1:berries\n""2:rose\n""3:apricot\n")
        plantlist=get_plant_from_file("plants.json")
        pb=plantlist[int(choise)]
        np = Plant([pb.get("name"),pb.get("fertilizer_requirement"),pb.get("water_requirement"),pb.get("growth_speed"),pb.get("light_requirement"),pb.get("plant_type")])
        print(
            f"you have added {np.name} to your garden\n"
            f"it will grow {np.growth_speed} days\n"
            f"it will need {np.fertilizer_requirement[0]} to {np.fertilizer_requirement[1]} fertilizer\n"
            f"it will need {np.water_requirement[0]} to {np.water_requirement[1]} water\n"
            f"it will need {np.light_requirement[0]} to {np.light_requirement[1]} light\n"
        )
        spot = input("where do you want to add the plant?\n")
        while not spot.isnumeric() or not int(spot) <= 16 or not int(spot) > 0:
            spot = input("must be a number between 1 and 16\n")
        self.plants.insert(int(spot), np)

    def remove_plant(self):
        spot = input("where do you want to add the plant?\n")
        while not spot.isnumeric() or not int(spot) <= 16 or not int(spot) > 0:
            spot = input("must be a number between 1 and 16\n")
        self.plants.pop(int(spot))

    def water_plant(self, spot):
        self.plants[spot].water()

    def grow(self):
        self.time += 1
        [x.grow() for x in self.plants]

    def random_event(self):
        rand = random.randint(0, 100)

        if rand < 40:
            print("no event today")
        elif rand < 60:
            print("it rains today\n""no nead to water plants")
            [x.water() for x in self.plants]
        elif rand < 80:
            print("the sun shines brightly\n""water plants")
            [x.drain() for x in self.plants]
        elif rand < 90:
            print("ther is a parasite\n""trim the infected plant")
            rand =random.randint(0, len(self.plants)-1)
            self.plants[rand].damage(10)
        elif rand < 100:
            print("a storm comes in\n""it unrouts the garden")
            self.plants = []
    def pass_day(self):
        self.random_event()
        self.grow()
    def display(self):
        print(f"day {self.time}")
        print(f"----------\n {self.plants}")
    def play(self):
        print("wellcome to the garden\n")
        inp=input("what do you whant to name your garden?\n")
        while not inp.isprintable() or inp == "" or len(inp)>20:
            inp = input("input a valid name\n")
        self.name = inp
        print(f"your garden is called {self.name}")
        print("you have 10 days to build your garden")
        input("Press any key to continue...")
        for self.time in range(10):
            self.time += 1
            self.display()
            inp = input("1:add plant\n""2:remove plant\n""3:water plant\n")
            while inp != "1" and inp != "2" and inp != "3":
                print("wrong input")
                self.display()
                inp = input("1:add plant\n""2:remove plant\n""3:water plant\n")
            if inp == "1":
                self.add_plant()
