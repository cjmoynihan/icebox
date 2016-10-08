from bottle import route, run, request, template, static_file, get, post
import main

# Static Routes
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
    return template('index.tpl', ingredients=main.get_ingredients())

@route('/', method='POST')
def modify_ingredient():
    modification=request.forms.get('modification')
    ingredients=request.forms.getall('ingredients')
    ingredients=[ingredient.strip() for ingredient in ingredients]
    ingredients=request.forms.get('ingredients')
    ingredients=[ingredient.strip() for ingredient in ingredients.split(', ')]
    if modification=="add":
        for ingredient in ingredients:
            main.add_ingredient(ingredient)
    if modification=="remove":
        for ingredient in ingredients:
            main.remove_ingredient(ingredient)
    return homepage()

if __name__ == '__main__':
    run(host='127.0.0.1', port=8000, reloader=True, debug=True)
