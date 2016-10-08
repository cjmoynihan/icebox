import database
from bottle import route, run, template

db = database.Database()

# An Ingredient is a String
# A List of Ingredients (LOI) is a (Ingredient, ...)
# A Recipe is a (String, LOI, String)
# A List of Recipes is a (LOR) is a (Recipe, ...)


# check_ingredient: Ingredient -> Boolean
# check if user has an ingredient
def check_ingredient(ingredient):
	return db.check_ingredient(ingredient)

# add_ingredient: Ingredient
# adds an ingredient into the users database
def add_ingredient(ingredient):
	db.add_ingredient(ingredient)

# remove_ingredient: Ingredient
# removes an ingredient from the users database
def remove_ingredient(ingredient):
	db.remove_ingredient(ingredient)

# get_recipes: -> LOR
# finds recipes that can be created from the users ingredients
def get_recipes():
	recipe_list = db.get_recipes()
	possible_recipes = []
	for recipe in recipe_list:
		if compare_ingredients(recipe.ingredients):
			possible_recipes.append(recipe)
	return possible_recipes
		
def print_recipes():
        return '\n'.join((name for (name, ingredients) in get_recipes()))

# compare_ingredients: LOI LOI -> Boolean
# determines if a recipe can be created from user ingredients
def compare_ingredients(recipe_ingredients, user_ingredients=None):
	if user_ingredients==None:
		user_ingredients=db.get_ingredients()
	return set(user_ingredients).issuperset(recipe_ingredients)

# get_ingredients: -> LOI
# return a List of the user's Ingredients
def get_ingredients():
	return db.get_ingredients()
	    
# render main html file
@route('/index/')
def render_page():
	return template("index.html")

if __name__ == "__main__":
    run(host = 'localhost', port = 8080)

# run(host = 'localhost', port = 8080)
