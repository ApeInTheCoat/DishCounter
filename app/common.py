import json

recipes = None


def get_recipes(json_file):
    global recipes
    if not recipes:
        with open(json_file, 'r', encoding='UTF8') as cookbook:
            cookbook = json.load(cookbook)
            recipes = cookbook['recipes']

    return recipes


def assert_fridge_is_valid(fridge):
    if not isinstance(fridge, dict):
        raise TypeError(f'Invalid fridge, expected dict, instead got: {type(fridge)}')
    for name, count in fridge.items():
        if not (isinstance(name, str) and isinstance(count, int)):
            raise TypeError(f'Invalid fridge, expected fridge.items() to be (str, int), instead got: '
                            f'({type(name)},{type(count)})')


def count_dishes(recipes, fridge):
    dishes = []
    for recipe in recipes:
        count = float('inf')
        for component in recipe['components']:
            item = component['item']
            count = min(count, fridge.get(item, 0) // component['q'])
            if count == 0:
                break
        if count:
            dishes.append({recipe['name']: count})
    return dishes
