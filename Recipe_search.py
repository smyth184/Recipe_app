import requests

# welcome message
print('\nWelcome to our Recipe Finder!')


# Recipe search function
def recipe_search(ingredient, exclusions, cuisine_type, meal_type):
    app_id = '7a360a89'
    app_key = 'd8cc8b979a47905b2f875163868ab2b1'
    parameters = {
        'cuisineType': cuisine_type,
        'mealType': meal_type,
    }
    try:
        result = requests.get(
            'https://api.edamam.com/search?q={}&app_id={}&app_key={}&excluded={}'.format(ingredient, app_id,
                                                                                         app_key,
                                                                                         exclusions,
                                                                                         ),
            params=parameters
        )
        result.raise_for_status()  # Raise an exception if the request was unsuccessful

        # Return the list of different recipes
        recipe_list = result.json()
        return recipe_list['hits']
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the API request: {str(e)}")
        return []


def userinput():
    # Prompt user for main ingredient
    ingredient = input('\nPlease enter an ingredient: ')
    # Prompt user for excluded ingredients
    exclusions = input('\nAny food allergies? ')
    # Prompt user for calories
    meal_type = input('\nPlease enter a meal type, e.g Breakfast')
    # Prompt user for meal type
    cuisine_type = input('\nWhat cuisine type would you like? e.g chinese etc: ')
    # Get results from API
    results = recipe_search(ingredient, exclusions, cuisine_type, meal_type)

    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])
        print("Ingredients:")
        print(str(recipe['ingredients']))
        print("Calories:")
        print(int(recipe['calories']))
        print()

    # asking the user if they would like to save the recipe
    print("-------------------------------------------")
    write = input('Would you like to save the recipe to a file? Y/N: ').upper()

    if write == 'Y':
        with open('my_recipe.txt', 'w+') as text_file:
            label = recipe['label']
            website = recipe['url']
            text_file.write(label + '\n' + website)
            print('Recipe successfully saved!')
    else:
        print('\nYou have selected "N", recipe not saved')


userinput()
