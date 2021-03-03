from flask import Flask, render_template, jsonify, request, redirect
import random

app = Flask(__name__)

ingredients = ['flour', 'sugar', 'shortening', 'cherries', 'butter' ]

recipes = {
    'cherry': ['flour', 'sugar', 'shortening', 'cherries', 'butter'],
    'apple': ['flour', 'sugar', 'shortening', 'apple', 'butter'],
    'pumpkin': ['flour', 'sugar', 'shortening', 'pumpkin', 'butter', 'evaporated milk']
}

@app.route('/')
def hello():
    return 'Hello, world!'

@app.route('/greeting/<name>')
def greeting(name):
    return render_template('index.html', name = name)

@app.route('/pie')
def pie():
    return jsonify({'pie ingredient': ingredients[random.randrange(len(ingredients))]})

@app.route('/recipe', methods = ['GET', 'POST'])
def recipe():
    if request.method == 'GET': 
        return render_template('recipe.html', name = 'cherry', ingredients = ingredients)
    if request.method == 'POST':
        new_ingredient = request.form['ingredient']
        ingredients.append(new_ingredient)
        return redirect('/recipe')

@app.route('/recipe/<pie>', methods = ['GET', 'POST'])
def specific_recipe(pie):
    if request.method == 'GET':
        return render_template('recipe.html', name = pie, ingredients = recipes[pie])
    if request.method == 'POST':
        new_ingredient = request.form['ingredient']
        recipes[pie].append(new_ingredient)
        return redirect(f'/recipe/{pie}')