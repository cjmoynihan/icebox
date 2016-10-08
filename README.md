# icebox
Finds recipes from ingredients


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
      
