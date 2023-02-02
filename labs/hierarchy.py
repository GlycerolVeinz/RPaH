import abc

# tea / coffee

# same movements
# 1.boil water
# 2. add -special ingredient- to mug
# 3. add water to mug
# 4. add bonus ingredients

# tea 2.: add teabag

# coffee 2.: add coffee


class HotDrink(abc.ABC):
    def __init__(self, bonus_ingredients: list):
        self.bonus_ingredients = bonus_ingredients
        

    def boil_water(self):
        print("Boiling water...")

    # def add_main_in(self):
    #     raise NotImplemented("You must choose what drink you want!")

    @classmethod
    def add_main_in(cls):
        print(f"Putting a {cls.main_in}")

    def add_water(self):
        print("Adding water to a mug...")

    def add_bonus_in(self):
        print("Adding your chosen ingredients...")
        for i in self.add_ingredients:
            print(f"Adding {i}...")
    
    def prepare_drink(self):
        self.boil_water()
        self.add_main()
        self.add_water()
        self.add_bonus_in()


class Tea(HotDrink):
    main_in = "teabag"

class Coffee(HotDrink):
    main_in = "coffee"

class Kokoa(HotDrink):
    main_in = "cocoa"

    def boil_water(self):
        print("Heating up milk...")

    def add_water(self):
        print("Adding milk to a mug...")


if __name__ == "__main__":
    drink = Kokoa("honey")
    drink.prepare_drink()