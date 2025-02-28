growth_stage = {
    "sprout": 0,
    "seedling": 1,
    "vegetative": 2,
    "buding": 3,
    "flowering": 4,
    "harvest": 5,
    "dead": 6,
}

PlantDict = {
    "name": str,
    "fertilizer_amount": int,
    "fertilizer_requirement": tuple[int,int],
    "water_amount": int,
    "water_requirement": tuple[int,int],
    "growth_speed": int,
    "growth_stage": str,
    "light_amount": int,
    "light_requirement": tuple[int,int],
    "health": int,
    "age": int,
    "plant_type": str
}
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
    def __init__(self, plant_base:Plant_base):
        self.name = plant_base.get("name")
        self.fertilizer_amount = 0
        self.fertilizer_requirement = plant_base.get("fertilizer_requirement")
        self.water_amount = 10
        self.water_requirement = plant_base.get("water_requirement")
        self.growth_speed = plant_base.get("growth_speed")
        self.growth_stage = 0
        self.light_amount = 10
        self.light_requirement = plant_base.get("light_requirement")
        self.age = 0
        self.health = 100
        self.plant_type = plant_base.get("plant_type")
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
