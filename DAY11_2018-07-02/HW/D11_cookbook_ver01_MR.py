# 2018-07-03, M. Ryś
# cookbook - 1st conception


class Ingredient:

    def __init__(self, name, unit_of_amount):
        self.name = name
        self.unit_of_amount = unit_of_amount

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Recipe:
    categories = ('breakfast', 'dinner', 'supper', 'dessert')

    def __init__(self,
                 title='Unknown recipe',
                 description='Unknown description how to prepare meal.',
                 time_of_preparation='Unknown time',
                 persons='Unknown amount',
                 category='dinner'):
        self.ingredient_list = {}
        self.description = description
        self.title = title
        self.time_of_preparation = time_of_preparation
        self.persons = persons
        # TODO: add here fail category check
        self.category = category

    def add_ingredient(self, ingredient_to_add, how_many=1):
        try:
            self.ingredient_list[ingredient_to_add]
        except KeyError:
            self.ingredient_list[ingredient_to_add] = float(how_many)
        else:
            self.ingredient_list[ingredient_to_add] += float(how_many)

    def update_how_to_prepare(self, input_text):
        self.description = input_text

    def update_title(self, title):
        self.title = title

    def update_time_of_preparation(self, time, unit='minutes'):
        self.time_of_preparation = str(time) + ' ' + str(unit)

    def update_persons(self, amount_of_persons):
        self.persons = int(amount_of_persons)

    def update_category(self, new_category):
        while True:
            if new_category in self.categories:
                self.category = new_category
                print(f'OK. New cattegory is: {new_category}')
                break
            else:
                print('Give correct category. Must be one from these:')
                for cat in self.categories:
                    print(cat)
                new_category = input('New category is: ')

    def __str__(self):
        # + ': ' + self.description[0:19] + '...'
        return str(self.title)

    def __repr__(self):
        return self.__str__()


class Cookbook:
    def __init__(self):
        #               key=recipe, value=category
        self.recipies = {}

    def add_recipe(self, recipe):
        self.recipies[recipe] = recipe.category

    def print_all(self):
        for recipe in self.recipies.keys():
            print(recipe, ':', self.recipies[recipe])

    def print_by_category(self, category):
        other_categories = 0
        if category in Recipe.categories:
            for recipe in self.recipies.keys():
                if self.recipies[recipe] == category:
                    print('"', recipe, '": ', self.recipies[recipe], sep='')
                else:
                    other_categories += 1
            if other_categories:
                print(f'(There are recipes in other categories: '
                      f'{other_categories})')
        else:
            print(f'"{category}" is not a proper category. '
                  f'It must be one of them:')
            print(str(Recipe.categories))


    def print_recipe(self, recipe_name, portions=1):
        for recipe_in_db in self.recipies.keys():
            if recipe_name == recipe_in_db.__repr__():

                default_portion = recipe_in_db.persons
                portions_food_factor = portions / default_portion

                print(50 * '=')
                print('== ', sep='', end='')
                print(recipe_in_db.title, ' ', sep='', end='')
                frame_len = 50 - 4 - len(recipe_in_db.title)
                if frame_len > 0:
                    print(frame_len * '=')
                else:
                    print('==')
                print(50 * '=')
                print('Ingredients for ',
                      default_portion * portions_food_factor,
                      'persons:')
                for ingredient in recipe_in_db.ingredient_list.keys():
                    print(ingredient, ': ', sep='', end='')
                    print(portions_food_factor * recipe_in_db.ingredient_list[ingredient], ' ', sep='', end='')
                    print(ingredient.unit_of_amount)
                print(50 * '-')
                print('Time to prepare for ', default_portion, ' persons: ', sep='', end='')
                print(recipe_in_db.time_of_preparation)
                print('Persons', ': ', sep='', end='')
                print(portions_food_factor * recipe_in_db.persons)
                print(50 * '=')
                print(recipe_in_db.description)
                print(50 * '=')
                print(50 * '=')

    def __str__(self):
        return str(self.recipies)

    def __repr__(self):
        return self.__str__()

# ------------------------------------------------------------------------------

potato_small_kg = Ingredient('potato_small', 'kg')
salt_pinch = Ingredient('salt', 'pinch')
print(potato_small_kg, salt_pinch)

# 1st recipe
recipe_01 = Recipe(category='dinner')
recipe_01.add_ingredient(potato_small_kg, 5)
recipe_01.add_ingredient(salt_pinch, 2)
recipe_01.update_title('French Potato Puree')
recipe_01.update_how_to_prepare('1. Boil water with salt.\n'
                                '2. Add potatoes.\n'
                                '3. Wait some time\n'
                                '4. Check if it is ok.\n'
                                '5. Pull out.\n'
                                '6. Eat.')
recipe_01.update_persons(10)
recipe_01.update_time_of_preparation(30)

# 2nd recipe
recipe_02 = Recipe(category='dinner')
recipe_02.add_ingredient(potato_small_kg, 12)
recipe_02.add_ingredient(salt_pinch, 4)
recipe_02.update_title('Polish Potato Puree')
recipe_02.update_how_to_prepare('1. Boil water with salt.\n'
                                '2. Add potatoes.\n'
                                '3. Wait some time\n'
                                '4. Check if it is ok.\n'
                                '5. Pull out.\n'
                                '6. Eat.')
recipe_02.update_persons(1)
recipe_02.update_time_of_preparation(90)

# 3rd recipe
recipe_03 = Recipe(category='supper')
recipe_03.add_ingredient(potato_small_kg, 20)
recipe_03.add_ingredient(salt_pinch, 0.5)
recipe_03.update_title('German Potato Puree')
recipe_03.update_how_to_prepare('1. Boil water with salt.\n'
                                '2. Add potatoes.\n'
                                '3. Wait some time\n'
                                '4. Check if it is ok.\n'
                                '5. Pull out.\n'
                                '6. Eat.')
recipe_03.update_persons(2)
recipe_03.update_time_of_preparation(5)

print(recipe_01, recipe_02, recipe_03)
print(52*'-')

cookbook_mr = Cookbook()
cookbook_mr.add_recipe(recipe_01)
cookbook_mr.add_recipe(recipe_02)
cookbook_mr.add_recipe(recipe_03)

print(cookbook_mr.recipies)
print(52 * '-')

cookbook_mr.print_all()
print('\n')
print('>> Print selected recipe for chosen number of persons/portions:')
cookbook_mr.print_recipe('German Potato Puree', 10)

print()
print()
# print by category
cookbook_mr.print_by_category('dinner')
print()
cookbook_mr.print_by_category('ice cream')
