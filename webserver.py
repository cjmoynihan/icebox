from bottle import route, run, request
import main

@route('/')
def homepage():
    return template('index.tpl')

@route('/', method='POST')
def modify_ingredient():
    modification=request.forms.get('modification')
    ingredients=request.forms.get('ingredients')
    ingredients=[ingredient.strip() for ingredient in ingredients.split(', ')
    if modification=="add":
        for ingredient in ingredients:
            main.add_ingredient(ingredient)
    if modification=="remove":
        for ingredient in ingredients:
            main.remove_ingredient(ingredient)
    return homepage()

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
