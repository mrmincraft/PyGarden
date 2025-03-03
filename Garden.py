import random


from FilesUtiles import get_plant_from_file

from Plant import Plant, Plant_base

# should have been the structure from the start 3/3/2025 11:44
# default_plant_dict={
#     "0": None or dict,
#     "1": None or dict,
#     "2": None or dict,
#     "3": None or dict,
#     "4": None or dict,
#     "5": None or dict,
#     "6": None or dict,
#     "7": None or dict,
#     "8": None or dict,
#     "9": None or dict,
#     "10": None or dict,
#     "11": None or dict,
#     "12": None or dict,
#     "13": None or dict,
#     "14": None or dict,
#     "15": None or dict,
# }

class Garden():
    def __init__(self, name="", plants=None or dict, time = 0):
        if plants is None:
            plants = []
            [plants.append(None) for _ in range(16)]
        else:
            plantlist = get_plant_from_file("plant_base.json")

            for key in plants:
                if plants[key] is not None:
                    plb = plantlist[int(key)]
                    np = Plant(plb)
                    self.plants[spot] = np



        plantslist = []
        self.name = name
        self.plants = [plantslist.append(None) for _ in range(16)]
        self.time = time


    def __str__(self):
        return f"{self.name}{self.plants}{self.time}"

    def to_dict(self):
        savedict={}
        for index, x in enumerate(self.plants):
            if x is not None:
                savedict[f"{index}"]= x.__dict__
            else :
                savedict[f"{index}"]= None
        return {
            "name":self.name,
            "plants":savedict,
            "time":self.time
        }

    def select_spot(self,message:str):
        spot = input(f"where do you want to {message}?\n")
        while not spot.isnumeric() or not int(spot) <= 16 or not int(spot) > 0:
            print("invalid input")
            spot = input("input must be a number between 1 and 16\n")
        return int(spot)-1

    def spotistaken(self,spot:int):
            if self.plants[spot] is not None:
                return True
            else:
                return False

    def add_plant(self):
        choise = input("what plant do you want to add?\n""1:berries\n""2:rose\n""3:apricot\n")
        while not choise.isnumeric() or not int(choise) <= 3 or not int(choise) > 0:
            print("input must be a number")
            choise = input("what plant do you want to add?\n""1:berries\n""2:rose\n""3:apricot\n")
        plantlist=get_plant_from_file("plant_base.json")
        pb=plantlist[int(choise)]
        np = Plant(pb)
        print(
            f"you have added {np.name} to your garden\n"
            f"it will grow in {np.growth_speed} days\n"
            f"it will need {np.fertilizer_requirement[0]} to {np.fertilizer_requirement[1]} fertilizer\n"
            f"it will need between {np.water_requirement[0]}% and {np.water_requirement[1]}% humidity\n"
            f"it will need between {np.light_requirement[0]}% and {np.light_requirement[1]}% light\n"
        )
        spot = self.select_spot("add it to the garden")
        while self.spotistaken(spot):
            print("spot is taken")
            spot = self.select_spot("add it to the garden")
        self.plants[spot] = np

    def remove_plant(self):
        self.plants.pop(self.select_spot("remove"))

    def water_plant(self):
        spot=self.select_spot("spray water")
        while not self.spotistaken(spot):
            print("spot is empty")
            spot=self.select_spot("spray water")
        self.plants[spot].water()

    def grow(self):
        self.time += 1
        [x.grow() for x in self.plants if x is not None]

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
        print(f"----------\n")
        [x.display() for x in self.plants if x is not None]

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
            elif inp == "2":
                self.remove_plant()
            elif inp == "3":
                self.water_plant()
    def test(self):
        self.name = "test"
        plantlist = get_plant_from_file("plant_base.json")
        pb = plantlist[0]
        self.plants.pop(10)
        self.plants.insert(10, Plant(pb))
        self.plants.pop(5)
        self.plants.insert(5, Plant(pb))
        self.plants.pop(1)
        self.plants.insert(1, Plant(pb))
        self.plants.pop(15)
        self.plants.insert(15, Plant(pb))
        self.plants.pop(0)
        self.plants.insert(0, Plant(pb))


