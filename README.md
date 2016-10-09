# icebox is a tool for keeping track of your fridge so you don't have to
Files
database.py
    Manages the database, which runs in sqlite3
    Schema is two tables
        user_ingredients:
        |ingredient|
        ingredient is primary key text
        
        recipes:
        |id|recipe name|ingredients|instructions|
        id is primary key
        recipe name is text
        ingredients is text
        instructions is text
        (recipe name, ingredients, instructions) has unique constraint

        links:
        |url|
        url is primary key text

    Manages back end by feeding information from db to main.py, by recieving data to store from allrecipes.py, and by storing links scraped by allrecipes.py

main.py
    The interface for recieving and processing information related to ingredients and recipes

webserver.py
    A bottle server that runs the website out of views, and manages feeding information between the user and the client

allrecipes.py
    A web scrapper that recursively searches through the allrecipes website, ignoring links its already found

imagereader.py
static/
    Holds various folders for unchanging data that is referenced by bottle and website
    webserver.py handles redirection to this folder, to reference inside template or bottle, just use foo.bar, not static/images/foo.bar
    css/
    fonts/
    images/
    js/
    sass/

views/
    Holds the webpages and templates that webserver.py references in creating the website/webserver


Various functions in main.py
# add ingredient to user ingredient database
add_ingredient(ingredient)
  if ingredient not in user inventory
    add ingredient
 
# remove ingredient from user ingredient database
remove_ingredient(ingredient)
  if ingredient in user inventory
    remove ingredient entry

# check if ingredient is in user's inventory database
check_ingredient(ingredient)
  if ingredient in user inventory
    return ingredient
   
# generate a list of recipes given the list of user ingredients
generate_recipes(list_of_ingredients) 
  ingredients = set_ingredients
  recipe_list = {}
  for recipe in recipes
    if set_ingredients is superset of recipe_ingredients
     add recipe to recipe_list
  return recipe_list
  
# add recipe into recipes database
add_recipe(name, ingredient_list, **kwargs)
  add recipe into database
      
