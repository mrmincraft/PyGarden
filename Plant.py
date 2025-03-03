growth_stage = {
    0:"sprout",
    1:"seedling",
    2:"vegetative",
    3:"buding",
    4:"flowering",
    5:"harvest",
    6:"dead",
}

PlantDict = {
    "name": str,
    "fertilizer_amount": int,
    "fertilizer_requirement": tuple[int,int],
    "water_amount": int,
    "water_requirement": tuple[int,int],
    "growth_speed": int,
    "growth_stage": int,
    "light_amount": int,
    "light_requirement": tuple[int,int],
    "health": int,
    "age": int,
    "plant_type": str
}
Plant_signature = (str, int, tuple[int,int], int, tuple[int,int], int, int, int, tuple[int,int], int, int, str)
Plant_base ={
    "name": str,
    "fertilizer_requirement": tuple[int,int],
    "water_requirement": tuple[int,int],
    "growth_speed": int,
    "light_requirement": tuple[int,int],
    "plant_type": str
  }
def clamp(n, min_value, max_value):
    return max(min_value, min(n, max_value))

class Plant:
    def __init__(self, plant_base: Plant_base or PlantDict ):

        self.name = plant_base.__getitem__("name")
        self.fertilizer_requirement = plant_base.__getitem__("fertilizer_requirement")
        self.water_requirement = plant_base.__getitem__("water_requirement")
        self.growth_speed = plant_base.__getitem__("growth_speed")
        self.light_requirement = plant_base.__getitem__("light_requirement")
        self.plant_type = plant_base.__getitem__("plant_type")
        if plant_base is PlantDict:
            self.fertilizer_amount = plant_base.__getitem__("fertilizer_amount")
            self.water_amount = plant_base.__getitem__("water_amount")
            self.growth_stage = plant_base.__getitem__("growth_stage")
            self.light_amount = plant_base.__getitem__("light_amount")
            self.age = plant_base.__getitem__("age")
            self.health = plant_base.__getitem__("health")
        else:
            self.fertilizer_amount = 0
            self.water_amount = 10
            self.growth_stage = 0
            self.light_amount = 10
            self.age = 0
            self.health = 100

    def __str__(self):
        return f"{self.name}{self.age}{self.fertilizer_amount}{self.fertilizer_requirement}{self.water_amount}{self.water_requirement}"

    def health_check(self):
        if self.health <= 0:
            self.growth_stage = 6

    def get_growth_stage(self):
        return self.growth_stage

    def grow(self):
        self.age += 1
        if self.water_amount < self.water_requirement[0] or self.water_amount > self.water_requirement[1]:
            self.health -= 10
            self.health_check()
            print('water problem')
            return
        if self.fertilizer_amount < self.fertilizer_requirement[0] or self.fertilizer_amount > self.fertilizer_requirement[1]:
            self.health -= 10
            self.health_check()
            print('fertilizer problem')
            return
        if self.light_amount < self.light_requirement[0] or self.light_amount > self.light_requirement[1]:
            self.health -= 10
            self.health_check()
            print('light problem')
        if self.age >= self.growth_speed:
            self.growth_stage += 1
            self.health= clamp(0,self.health+10,100)

    def water(self):
        self.water_amount += 1

    def fertilize(self):
        self.fertilizer_amount += 1

    def light(self):
        self.light_amount += 1

    def drain(self):
        self.water_amount -= 1

    def fertilize_drain(self):
        self.fertilizer_amount -= 1

    def damage(self, amount):
        self.health -= amount
        self.health_check()

    def display(self):
        print(growth_stage.__getitem__(self.growth_stage))

