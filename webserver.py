from bottle import route, run, request, template, static_file, get, post
import main
from database import Recipe
foods=('bread','muffin','pudding','squash', 'biscuit', 'cake', 'cookies', 'fudge', 'salad')

image_paths = {
"apple pie" : "applePie.jpg" , "cheese burger" : "cheeseBurger.jpg" , "crepes" : "crepes.jpg" , "egg" : "egg.jpg" , "french fries" : "frenchFries.jpg" , "hamburger" : "hamBurger.jpg" , "ham sandwich" : "hamSandwich.jpg" , "kimchi" : "kimchi.jpg" , "mashed potatoes" : "mashedPotatoes.jpg" , "omelette" : "omelette.jpg" , "pancake" : "pancake.jpg" , "pizza" : "pizza.png" , "steak" : "steak.jpg" , "sushi" : "sushi.jpg" , "yogurt parfait" : "yogurtParfait.jpg","pancake":"pancake.jpg", "chicken" : "bakedChicken.jpg" , "beef stroganoff" : "beefStroganoff.jpg" , "blueberry pie" : "blueberrypie.jpg" , "chicken and dumplings" : "chickenandDumplings.jpg" , "chicken spaghetti" : "chickenSpaghetti.jpg" , "cinnamon buns" : "cinnamonBuns.jpg" , "cheese ball" : "cheeseBall.jpg" , "cupcake" : "cupcake.jpg" , "pork chop" : "porkChop.jpg" , "pork loin" : "porkLoin.jpg" , "pot roast" : "potRoast.jpg" , "pumpkin cheesecake" : "pumpkinCheesecake.jpg" , "salmon" : "salmon.jpg" , "shrimp dip" : "shrimpDip.jpg" , "shrimp scampi" : "shrimpScampi.jpg" , "tofu" : "tofu.jpg",
}
for food in foods:
    image_paths[food]=food+'.jpg'

def get_path(recipe_name):
    for (food, path) in image_paths.iteritems():
        if food in recipe_name:
            return path
    return "generic_img.jpg"

# Static Routes
# Redirects all files to the static folder
@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get('/<filename:re:.*\.(jpg|png|gif|ico|svg)>')
@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/images')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')

@route('/')
def homepage():
    recipes = main.get_recipes()
    recipes = [Recipe(recipe.name, [ingredient.strip("u'") for ingredient in recipe.ingredients], [instruction.strip("u'").strip("[u'").strip("']") for instruction in recipe.instructions.split(', ')]) for recipe in recipes]
    return template('index.tpl', ingredients=main.get_ingredients(), recipes=tuple(recipes), get_path=get_path)

# Takes a POST and either adds or removes ingredients
@route('/', method='POST')
def modify_ingredient():
    modification=request.forms.get('modification')
    ingredients=request.forms.getall('ingredients')
    ingredients=[ingredient.strip() for ingredient in ingredients]
    ingredients=request.forms.get('ingredients')
    ingredients=[ingredient.strip() for ingredient in ingredients.split(', ')]
    if modification=="add":
        for ingredient in ingredients:
            if ',' in ingredient:
                for i in [i.strip() for i in ingredient.split(',')]:
                    main.add_ingredient(i)
            else:
                main.add_ingredient(ingredient.strip())
    if modification=="remove":
        for ingredient in ingredients:
            main.remove_ingredient(ingredient)
    return homepage()


if __name__ == '__main__':
    run(host='0.0.0.0', port=80, reloader=True)
