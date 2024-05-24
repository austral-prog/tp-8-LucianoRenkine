from sets_categories_data import ALCOHOLS

def clean_ingredients(dish_name, dish_ingredients):
    a = set(dish_ingredients)
    return (dish_name, a)

def check_drinks(drink_name, drink_ingredients):
    a = set(drink_ingredients)
    b = a.intersection(ALCOHOLS)
    if len(b) == 0:
        return f"{drink_name} Mocktail"
    else:
        return f"{drink_name} Cocktail"
