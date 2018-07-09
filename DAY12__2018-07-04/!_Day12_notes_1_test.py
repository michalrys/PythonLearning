# 2018-07-02, M. Ryś
# InfoShare: day 12.
#
# ------------------------------------------------------------------------------

class Ingredient:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return self.__str__()


class Recipe:
    def __init__(self):
        self.ingredients = []

    def add(self, ingredient, how_many):
        for item in range(how_many):
            self.ingredients.append(ingredient)

    def __str__(self):
        return str(self.ingredients)

    def __repr__(self):
        return self.__str__()


potatoe_long = Ingredient('potatoe_long', 10)
potatoe_short = Ingredient('potatoe_short', 4)
salt = Ingredient('salt', 2)

recipe_1 = Recipe()
recipe_1.add(potatoe_long, 5)
recipe_1.add(potatoe_short, 7)
recipe_1.add(salt, 3)

print(recipe_1)

