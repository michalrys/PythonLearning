# 2018-07-06, M. Ryś
# cookbook - 2ND conception


class Ingredient:
    __category = []
    __unit = []

    @classmethod
    def category_add(cls, value):
        cls.__category.append(value)
        list(set(cls.__category))

    @classmethod
    def unit_add(cls, value):
        cls.__unit.append(value)
        list(set(cls.__unit))

    def __init__(self):
        self.__name = ''
        self.__kind = ''
        self.__mass_unit = 'kg'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = str(value)

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        if value in Ingredient.__category:
            self.__kind = value
        else:
            self.__kind = 'kg'

    @property
    def mass_unit(self):
        return self.__mass_unit

    @mass_unit.setter
    def mass_unit(self, value):
        if value in Ingredient.__unit:
            self.__mass_unit = value
        else:
            self.__kind = 'unknown'

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return self.__str__()


class Recipe:
    __category = []

    @classmethod
    def category_add(cls, value):
        cls.__category.append(value)
        list(set(cls.__category))

    @classmethod
    def category_remove(cls, value):
        if value in cls.__category:
            cls.__category.remove(value)
        else:
            raise ValueError

    def __init__(self):
        self.__title = 'Unknown recipe'
        self.__description = 'Unknown description how to prepare meal.'
        self.__persons = 'Unknown amount'
        self.__kind = ''
        self.__ingredients = {}

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = str(value)

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = str(value)

    @property
    def kind(self):
        return self.__kind

    @property
    def persons(self):
        return self.__persons

    @persons.setter
    def persons(self, value):
        if bool(int(value)):
            self.__persons = int(value)
        else:
            raise TypeError

    @kind.setter
    def kind(self, value):
        if value in Recipe.__category:
            self.__kind = str(value)
        else:
            self.__kind = Recipe.__category[0]

    @property
    def ingredients(self):
        return self.__ingredients

    def add_ingredient(self, ingredient, how_many=1.0):
        if isinstance(ingredient, Ingredient):
            self.__ingredients[ingredient] = float(how_many)
        else:
            print('Wrong ingredient type.')
            return

    def __str__(self):
        return f'"{self.title}", {self.kind}'

    def __repr__(self):
        return self.__str__()


class Cookbook:
    def __init__(self):
        self.__name = 'Unknown cookbook'
        self.__recipe = {}
        self.__category = {}
        self.__persons = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def kind(self):
        return self.__category

    @property
    def recipe(self):
        return self.__recipe

    @property
    def persons(self):
        return self.__persons

    @recipe.setter
    def recipe(self, new_recipe_to_add):
        if isinstance(new_recipe_to_add, Recipe):
            recipe_id = 1
            if len(self.__recipe) == 0:
                self.__recipe[recipe_id] = new_recipe_to_add
                self.__category[recipe_id] = new_recipe_to_add.kind
                self.__persons[recipe_id] = new_recipe_to_add.persons
            else:
                recipe_id += len(self.__recipe)
                self.__recipe[recipe_id] = new_recipe_to_add
                self.__category[recipe_id] = new_recipe_to_add.kind
                self.__persons[recipe_id] = new_recipe_to_add.persons

    def recipe_remove(self, id_or_recipe_name_to_delete):
        try:
            recipe_id_to_delete = int(id_or_recipe_name_to_delete)
        except ValueError:
            recipe_name_to_delete = id_or_recipe_name_to_delete
            for idx, recipe in enumerate(self.__recipe.values(), 1):
                if recipe_name_to_delete == recipe.title:
                    print(f'\tRecipe: >>{self.recipe[idx]}<< was removed.')
                    del self.__recipe[idx]
                    del self.__category[idx]
                    del self.__persons[idx]
                    self.__recipe_renumber()
                    return
        else:
            if recipe_id_to_delete <= 0:
                print('Given ID must be > 1.')
                return
            else:
                if recipe_id_to_delete in self.__recipe.keys():
                    print(f'\tRecipe: >>'
                          f'{self.recipe[recipe_id_to_delete]}'
                          f'<< was removed.')
                    del self.__recipe[recipe_id_to_delete]
                    del self.__category[recipe_id_to_delete]
                    del self.__persons[recipe_id_to_delete]
                    self.__recipe_renumber()
                    return
                else:
                    print('There is no such recipe ID.')
                    return

    def __recipe_renumber(self):
        recipes_amount = len(self.__recipe)
        recipes_temporary_copy = {}
        category_temporary_copy = {}
        persons_temporary_copy = {}
        if not recipes_amount == 0:
            for idx, key in enumerate(self.recipe.keys(), 1):
                recipes_temporary_copy[idx] = self.recipe[key]
            for idx, key in enumerate(self.kind.keys(), 1):
                category_temporary_copy[idx] = self.kind[key]
            for idx, key in enumerate(self.persons.keys(), 1):
                persons_temporary_copy[idx] = self.persons[key]
        self.__recipe = recipes_temporary_copy
        self.__category = category_temporary_copy
        self.__persons = persons_temporary_copy
        del recipes_temporary_copy
        del category_temporary_copy
        del persons_temporary_copy

    def __print_recipe(self, id_or_name, identification, persons='default'):
        if id_or_name == 'id':
            recipe = self.recipe[identification]
            recipe_id = identification
        elif id_or_name == 'name':
            for idx, element in enumerate(self.recipe.values(), 1):
                if element.title == identification:
                    recipe = self.recipe[idx]
                    recipe_id = idx
        else:
            print('Wrong input data. Give recipe id or recipe name.')
            return

        recipe_title = recipe.title
        recipe_description = recipe.description

        if persons == 'default':
            recipe_persons = recipe.persons
            persons_factor = 1
        else:
            try:
                new_persons = float(persons)
            except ValueError:
                print('Error: amount of persons must be positive float number.')
                return
            else:
                if new_persons <= 0:
                    print('Number of persons must be > 0.')
                    return
                else:
                    recipe_persons = new_persons
                    persons_factor = new_persons / recipe.persons

        recipe_kind = recipe.kind
        recipe_ingred = recipe.ingredients

        recipe_ingred_name = {}
        recipe_ingred_kind = {}
        recipe_ingred_mass_unit = {}
        recipe_ingred_how_many = {}

        for idx, ingred in enumerate(recipe_ingred.keys(), 1):
            recipe_ingred_name[idx] = ingred.name
            recipe_ingred_kind[idx] = ingred.kind
            recipe_ingred_mass_unit[idx] = ingred.mass_unit
            recipe_ingred_how_many[idx] = recipe_ingred[ingred]

        print(f'== RECIPE {recipe_id} ', sep='', end='')
        print(50 * '=')
        print('\t', sep='', end='')
        print(recipe_title, ' ', sep='', end='\n')
        print(f'\t\tthis is {recipe_kind} for {recipe_persons:.0f} persons.')
        print(25 * '- ')
        print(recipe_description)
        print(25 * '* ')
        print(f'List of ingredients:')
        for idx, item in enumerate(recipe_ingred, 1):
            print(f'\t{idx}. '
                  f'{recipe_ingred_name[idx]} '
                  f'({recipe_ingred_kind[idx]}): '
                  f'{persons_factor * recipe_ingred_how_many[idx]:.2f} in '
                  f'[{recipe_ingred_mass_unit[idx]}]')

    def print(self, parameter='all', persons='default'):
        """Print recipes from cookbook
        :rtype: str
        :param str, float parameter: Recipe ID or recipe title.
        :param str,float persons: Number of persons - default or give number.
        :return:
        """
        if parameter == 'all':
            how_many_recipes = len(self.__recipe)
            print(f'Total number of recipes: {how_many_recipes}:')
            for idx in range(1, how_many_recipes + 1):
                print(f'== RECIPE {idx} ', sep='', end='')
                self.__print_recipe('id', idx, persons)
            return
        try:
            recipe_id_to_print = int(parameter)
        except ValueError:
            recipe_name_to_print = parameter
            for idx, recipe in enumerate(self.__recipe.values(), 1):
                if recipe_name_to_print == recipe.title:
                    self.__print_recipe('name', recipe_name_to_print, persons)
                    return
            print(f'Recipe {recipe_name_to_print} does not exist.')
        else:
            if recipe_id_to_print <= 0:
                print('Given ID must be > 1.')
                return
            else:
                if recipe_id_to_print in self.__recipe.keys():
                    self.__print_recipe('id', recipe_id_to_print, persons)
                    return
                else:
                    print('There is no such recipe ID.')
                    return

    def __str__(self):
        return f'"{self.name}": {self.recipe}'

    def __repr__(self):
        return self.__str__()


# define categories for ingredients and recipes
Ingredient.category_add('vegetable')
Ingredient.category_add('fruit')
Ingredient.category_add('meat')
Ingredient.category_add('spice')
Ingredient.unit_add('kg')
Ingredient.unit_add('g')
Ingredient.unit_add('dag')
Ingredient.unit_add('pinch')
Ingredient.unit_add('as you wish')
Recipe.category_add('breakfast')
Recipe.category_add('dinner')
Recipe.category_add('supper')
Recipe.category_add('dessert')

# create ingredients
potato = Ingredient()
potato.name = 'Potato small'
potato.kind = 'vegetable'
potato.mass_unit = 'dag'
print(potato, potato.kind, potato.mass_unit)

chicken_leg = Ingredient()
chicken_leg.name = 'Chicken leg small'
chicken_leg.kind = 'meat'
chicken_leg.mass_unit = 'kg'
print(chicken_leg, chicken_leg.kind, chicken_leg.mass_unit)

salt = Ingredient()
salt.name = 'Salt'
salt.kind = 'spice'
salt.mass_unit = 'pinch'
print(salt, salt.kind, salt.mass_unit)


# create recipes
recipe_01 = Recipe()
recipe_01.title = 'Chicken legs with potatoes'
recipe_01.kind = 'dinner'
recipe_01.persons = 2
recipe_01.description = '1. Wash meat, peel potatoes.\n' \
                        '2. Boil water with salt.\n' \
                        '3. Add potatoes.\n' \
                        '4. Fry meat, add salt.\n' \
                        '5. Wait 10 minutes.\n' \
                        '6. Check colour of meat - if brown = ready.\n' \
                        '7. Check potatoes with a fork - if soft = ready.\n' \
                        '8. Put on plate.\n' \
                        '9. Eat ;)'
recipe_01.add_ingredient(potato, 50)
recipe_01.add_ingredient(chicken_leg, 0.8)
recipe_01.add_ingredient(salt, 2)
print(recipe_01, recipe_01.persons, recipe_01.description,
      recipe_01.ingredients)

recipe_02 = Recipe()
recipe_02.title = 'Chicken legs with potatoes quicker'
recipe_02.kind = 'dinner'
recipe_02.persons = 2
recipe_02.description = '1. Boil water with potatoes, salt.\n' \
                        '2. Fry meat, add salt.\n' \
                        '3. After 13 minutes put on plate.\n' \
                        '4. Eat ;)'
recipe_02.add_ingredient(potato, 20)
recipe_02.add_ingredient(chicken_leg, 0.4)
recipe_02.add_ingredient(salt, 3)
print(recipe_02, recipe_02.persons, recipe_02.description,
      recipe_02.ingredients)

recipe_03 = Recipe()
recipe_03.title = 'Chicken legs BLEEE'
recipe_03.kind = 'supper'
recipe_03.persons = 4
recipe_03.description = '1. Fry meat, potatoes, add salt.\n' \
                        '2. After 30 minutes put on plate.\n' \
                        '3. Eat ;)'
recipe_03.add_ingredient(potato, 2000)
recipe_03.add_ingredient(chicken_leg, 2.5)
recipe_03.add_ingredient(salt, 8)
print(recipe_03, recipe_03.persons, recipe_03.description,
      recipe_03.ingredients)

recipe_04 = Recipe()
recipe_04.title = 'Chicken legs for army'
recipe_04.kind = 'dinner'
recipe_04.persons = 10
recipe_04.description = '1. Boil water with potatoes, salt.\n' \
                        '2. Fry meat, add salt.\n' \
                        '3. After 60 minutes put on plate.\n' \
                        '4. Eat ;)'
recipe_03.add_ingredient(potato, 8000)
recipe_03.add_ingredient(chicken_leg, 10)
recipe_03.add_ingredient(salt, 20)
print(recipe_04, recipe_04.persons, recipe_04.description,
      recipe_04.ingredients)

# create cookbook
print(82 * '-')
cb01 = Cookbook()
cb01.name = 'Polish cuisine'
cb01.recipe = recipe_01
cb01.recipe = recipe_02
cb01.recipe = recipe_03
cb01.recipe = recipe_04
print(cb01)
cb01.recipe_remove(1)
print(cb01)

print('++++++++++++')
print(cb01.kind)
print(cb01.persons)

# main print out ---------------------------------------------------------------
print('\n\n\n\n')
print('==== PRINT OUT ====\n')
# cb01.print('Chicken legs with potatoes quicker', 10)
cb01.print(2, 1)
# cb01.print()
