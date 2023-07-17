import requests
from pprint import pprint

# welcome message
print('\nWelcome to our Recipe Finder!')


# Recipe Search Function
def recipe_search(ingredient, exclusions, cuisine_type):
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = '7a360a89'
    app_key = 'a1a3c2a42b5495bea64d3e698c12632c	—'
    parameters = {
        'cuisineType': cuisine_type
    }
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}&excluded={}'.format(ingredient, app_id, app_key,
                                                                                     exclusions), params=parameters)

    # Return the list of different recipes
    recipe_list = result.json()

    return recipe_list['hits']


def userinput():
    # Prompt user for main ingredient
    ingredient = input('\nPlease enter an ingredient ')
    # Prompt user for excluded ingredients
    exclusions = input('\nAny food allergies?')
    # Prompt user for meal type
    cuisine_type = input('\nWhat cuisine type would you like? e.g chinese etc ')
    # Get results from API
    results = recipe_search(ingredient, exclusions, cuisine_type)

    for result in results:
        recipe = result['recipe']

        print(recipe['label'])
        print(recipe['uri'])
        print()
    # asking the user if they would like to save the recipe
    write = input('Would you like to save the recipe to a file? Y/N').upper()

    if write == 'Y':
        with open('my_recipe.txt', 'w+') as text_file:
            label = (recipe['recipe']['label'])
            website = (recipe['recipe']['url'])
            text_file.write(label + '\n ' + website)
    else:
        print('\nYou have selected "N", recipe not saved')


userinput()
