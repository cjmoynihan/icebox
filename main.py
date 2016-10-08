import database
from bottle import route, run, template

db = database.Database()


def check_ingredient(ingredient):
	return db.check_ingredient(ingredient)

def add_ingredient(ingredient):
	db.add_ingredient(ingredient)

def remove_ingredient(ingredient):
	db.remove_ingredient(ingredient)

def get_recipes():
	recipe_dict = db.get_recipes()
	possible_recipes = []
	for (name, ingredients) in recipe_dict:
		if compare_ingredients(db.get_ingredients(), ingredients):
			possible_recipes.append((name, ingredients))
        return possible_recipes
		
def print_recipes():
        return '\n'.join((name for (name, ingredients) in get_recipes()))

def compare_ingredients(user_ingredients, recipe_ingredients):
	return set(user_ingredients).issuperset(recipe_ingredients)

def get_ingredients():
	return db.get_ingredients()

@route('/index/')
def render_page():
	return template("index.html")


if __name__ == "__main__":
    run(host = 'localhost', port = 8080)
