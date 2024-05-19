from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}

def handler(request):
    recipe_dict = {}
    for dish, ingredients in DATA.items():
        ingredients_dict = {}
        for k, v in ingredients.items():
            ingredients_dict[k] = v
        recipe_dict[dish] = ingredients_dict

    context = {
        'recipe': recipe_dict
    }
    return render(request, 'calculator/index.html', context)
