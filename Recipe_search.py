import requests


def recipe_search(ingredient):
app_id = ''
app_key = ''
result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id,app_key))
data = result.json()


return data['hits']


def run():
ingredient = input('Enter an ingredient: ')


results = recipe_search(ingredient)
for result in results:
    recipe = result['recipe']
    print(recipe['label'])
    print(recipe['uri'])
    print()


run()
