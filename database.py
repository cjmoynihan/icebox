import sqlite3 as sql3

class Database():
	def __init__(self):
		# Initialize the connection to the server
		# c.execute("SQL COMMAND") to execute command
		# conn.commit() to commit all changes
		self.conn = sql3.connect("icebox.db")
		self.c = self.conn.cursor()
		self.check_tables()

	def check_tables(self):
		# This function creates the tables and makes sure they all exist!
		self.c.execute("CREATE TABLE IF NOT EXISTS user_ingredients (ingredient TEXT PRIMARY KEY)")
		self.c.execute("CREATE TABLE IF NOT EXISTS recipes (id INTEGER PRIMARY KEY, name TEXT, ingredients TEXT)")
		self.conn.commit()

	def get_ingredients(self):
		# Returns a list of ingredients
		self.c.execute("SELECT * FROM user_ingredients")
		return [row[0] for row in self.c.fetchall()]

	def add_ingredient(self, ingredient):
		# Adds ingredient to sql table
		self.c.execute("INSERT OR IGNORE INTO user_ingredients(ingredient) VALUES(?)", (ingredient,))
		self.conn.commit()

	def add_ingredients(self, ingredients):
		for ingredient in ingredients:
			self.add_ingredient(ingredient)

	def remove_ingredient(self, ingredient):
		# Removes ingredient from sql table
		self.c.execute("DELETE FROM user_ingredients WHERE ingredient = ?", (ingredient,))
		self.conn.commit()

	def check_ingredient(self, ingredient):
		# Get number of ingredients by name
		self.c.execute("SELECT count(*) FROM user_ingredients WHERE ingredient = ?", (ingredient,))
		# Convert number of results to TRUE/FALSE (0 is false, anything else is true)
		return bool(self.c.fetchone()[0])

	def get_recipes(self):
		# Return a dictionary of recipes as {"recipe name":[recipe detail 1, recipe detail 2, ...], "recipe name":[...], ...}
		self.c.execute("SELECT name, ingredients FROM recipes")
		"""
		[
			("recipe name": [ingredient 1, ingredient 2, ...]),
			("recipe name": [ingredient 1, ingredient 2, ...]),
		]
		"""
		return [(name, [food.strip("'") for food in ingredients[1:-1].split(', ')]) for (name, ingredients) in self.c.fetchall()]

	def add_recipe(self, recipe_name, ingredients):
		# Add a recipe (name, ingredients as list) to recipes
		self.c.execute("INSERT INTO recipes(name, ingredients) VALUES(?,?)", (recipe_name, str(tuple(ingredients))))
		self.conn.commit()