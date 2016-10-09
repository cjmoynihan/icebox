import sqlite3 as sql3

class Recipe():
	def __init__(self, name, ingredients, instructions):
		self.name=name
		self.ingredients=ingredients
		self.instructions=instructions

	def __str__(self):
		return "{0}: {1}".format(self.name, ', '.join(self.ingredients))

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
		self.c.execute("CREATE TABLE IF NOT EXISTS recipes (id INTEGER PRIMARY KEY, name TEXT, ingredients TEXT, instructions TEXT, unique(name,ingredients,instructions))")
                self.c.execute("CREATE TABLE IF NOT EXISTS links (url TEXT PRIMARY KEY)")
		self.conn.commit()

	def get_ingredients(self):
		# Returns a list of ingredients
		self.c.execute("SELECT * FROM user_ingredients")
		return [row[0] for row in self.c.fetchall()]

	def add_ingredient(self, ingredient):
		# Adds ingredient to sql table
		self.c.execute("INSERT OR IGNORE INTO user_ingredients(ingredient) VALUES(?)", (ingredient.lower(),))
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
		# Return a list of recipe name, ingredients, instructions
		self.c.execute("SELECT name, ingredients, instructions FROM recipes")
		recipe_list = [Recipe(name, [food.strip("'") for food in ingredients[1:-1].split(', ')], instructions) for (name, ingredients, instructions) in self.c.fetchall()]
		return recipe_list

	def add_recipe(self, recipe_name, ingredients, instructions):
		# Add a recipe (name, ingredients as list) to recipes
		self.c.execute("INSERT OR IGNORE INTO recipes(name, ingredients, instructions) VALUES(?,?,?)", (recipe_name, str(tuple((ingredient.replace(',', '') for ingredient in ingredients))), str(instructions)))
		self.conn.commit()

        def add_link(self, link):
            self.c.execute("INSERT OR IGNORE INTO links(url) VALUES(?)", (link,))
            self.conn.commit()

        def get_links(self):
            self.c.execute("SELECT * FROM links")
            return set([row[0] for row in self.c.fetchall()])

        def __fix_multiples(self):
            # Goes into recipes table and removes entries with identical entries
            print len(self.get_recipes())
            self.c.execute("""
                DELETE FROM recipes
                WHERE id not in (
                    SELECT min(id)
                    FROM recipes
                    group by name
                )
            """)
            self.conn.commit()

	def clear_ingredients(self):
	    self.c.execute("DELETE FROM user_ingredients")
	    self.conn.commit()
