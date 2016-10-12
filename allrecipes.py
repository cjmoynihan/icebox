# from lxml import html
import requests
from BeautifulSoup import BeautifulSoup
import re
import database
import sys

homepage = "http://allrecipes.com/recipes"
db = database.Database()

class Recipe():
        def __init__(self, name, ingredients, instructions, description=None, source_code=None):
                self.name=name
                self.ingredients=ingredients
                self.instructions=instructions
                self.description=description
                self.source_code=source_code

        def __str__(self):
                return "{0}: {1}".format(self.name, ', '.join(self.ingredients))

def get_recipe_links(baselink):
    # Gets the links for recipes from a allrecipes links with recipes on it!
    # Get webpage for link
    r=requests.get(baselink)
    # Create soup from text
    soup = BeautifulSoup(r.text)
    # Create set of links by finding only /recipe/ links
    links = set(soup.findAll('a', attrs={'href': re.compile("^/recipe/")}))
    # Change link tags to full links
    mod_links = ["http://allrecipes.com"+link['href'] for link in links]
    return mod_links

def get_info(recipe_link):
    # Creates a recipe object from the link by providing the name, ingredients, and instructions
    # First get name from last line in url
    recipe_name=recipe_link.strip('/').split('/')[-1].replace('-', ' ').replace('_', ' ')
    # Get ingredients from source code
    r=requests.get(recipe_link)
    soup = BeautifulSoup(r.text)
    # Create ingredient list
    ingredient_tags = set(soup.findAll('span', attrs={'itemprop': 'ingredients'}))
    ingredients = [ingredient.getText() for ingredient in ingredient_tags]
    # Get instructions
    step_tags = set(soup.findAll('li', attrs={'class':'step'}))
    steps = [step.getText() for step in step_tags if step.getText()]
#     print "Adding recipe {0}\nwith ingredients: {1}\nand instructions: {2}".format(recipe_name, ingredients, steps)
#     print '-----------------'
#     print '-----------------'
#     print '-----------------'
    return Recipe(recipe_name, ingredients, steps, source_code=r.text)

def process_links(baselink):
    mod_links=set(get_recipe_links(baselink))
    for link in mod_links.difference(db.get_links()):
        print "Adding link " + link
        # If the link is a photo (just a picture of a recipe) skip it
        if link.strip('/').split('/')[-2]=="photos":
            db.add_link(link)
            continue
        recipe = get_info(link)
        # If no instructios, don't add to db
        if recipe.instructions==[""] or recipe.instructions=="" or recipe.instructions=="[]" or recipe.instructions=="['']":
            pass
        else:
            db.add_recipe(recipe.name, recipe.ingredients, recipe.instructions)
        db.add_link(link)
        process_links(link)

def try_some_links(num):
    iterative_process_links(list(db.get_links())[:num])

def iterative_process_links(links):
    if isinstance(links, basestring):
        links=set()
        links.add(baselink)
    else:
        links=set(links)
    while links:
        # Take one link out of links
        # Apply iter_helper, adding to db and getting back new links
        # Get difference of new links and already added links
        # Add new links to links
        new_links = iter_helper(links.pop()).difference(db.get_links())
        links.update(new_links)
    
def iter_helper(link):
    # Processes a link, adding to db
    # Returns all following links
    print "Adding link " + link
    if link.strip('/').split('/')[-2]=="photos":
        # Just a photos link
        db.add_link(link)
        return set()
    recipe = get_info(link)
    # If no instructions, don't add to db
    if recipe.instructions==[""] or recipe.instructions=="" or recipe.instructions=="[]" or recipe.instructions=="['']":
        pass
    else:
        db.add_recipe(recipe.name, recipe.ingredients, recipe.instructions)
    db.add_link(link)
    return set(get_recipe_links(link))

if __name__ == "__main__":
    try_some_links(10)
#     sys.setrecursionlimit(3000)
#     process_links(homepage)
