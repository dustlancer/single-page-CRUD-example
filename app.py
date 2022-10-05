
from crypt import methods
from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from time import process_time_ns
from flask import Flask, render_template, request, redirect
from matplotlib.artist import get
from sympy import re
from data_manager import delete_category, update_item, get_items, delete_item, add_item, get_categories, add_category, delete_category, update_category
from models import Item


app = Flask(__name__)


menu = [
    {"title": "Items", "url": "/"},
    {"title": "Categories", "url": "/categories"}    
]


# Получение последнего используемого идиентификатора [Универсальная функция]
def get_last_id(list):
    ind = 0
    for i in list:
        if i['id'] >= ind: ind = i['id']
    
    return ind


#----------------  Роуты index.html

# Рендерит index, принимает запрос при добавлекнии записи
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        nam = request.form['item']
        cat = request.form['category']
        new_item = Item(get_last_id, nam, cat)
        add_item(new_item)
        print()
    return render_template("index.html", items=get_items(), categories= get_categories(), menu = menu, title="items")


# Удаление записи
@app.route("/delete_item/<id>")
def remove_item(id):
    delete_item(id)

    return redirect("/")


# Обновление записи
@app.route("/edit_item/<id>", methods=['POST', 'GET'])
def edit_item(id):
    name = request.form['new_name']
    cat = request.form['new_category']
    update_item(id, name, cat)

    return redirect("/")
    
    
#----------------  Роуты categories.html

# Рендер categories.html и добавление категории
@app.route("/categories", methods=['POST', 'GET'])
def categories():
    if request.method == 'POST':
        add_category(request.form['category'])
    return render_template("categories.html", categories=get_categories(), menu=menu, title="categories")


# Удаление категории
@app.route("/delete_category/<id>")
def remove_category(id):
    delete_category(id)
    
    return redirect("/categories")


# Редактирование категории
@app.route("/edit_category/<id>", methods=['POST'])
def edit_category(id):
    update_category(id, request.form['new_name'])

    return redirect("/categories")


if __name__ == "__main__":
    app.run(debug=True)