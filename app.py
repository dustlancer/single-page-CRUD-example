
from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from flask import Flask, render_template, request, redirect
from data_manager import update_item, get_items, delete_item, add_item
from models import Item


app = Flask(__name__)



# Рендерит index, принимает запрос при добавлекнии записи
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        new_item = Item(get_last_id, request.form['item'])
        add_item(new_item)
    return render_template("index.html", items=get_items())


# Получение последнего используемого идиентификатора
def get_last_id(list):
    ind = 0
    for i in list:
        if i['id'] >= ind: ind = i['id']
    
    return ind




# Удаление записи
@app.route("/delete_item/<id>")
def remove_item(id):
    delete_item(id)

    return redirect("/")



# Обновление записи
@app.route("/edit_item/<id>", methods=['POST', 'GET'])
def edit_item(id):
    update_item(id, request.form['new_name'])

    return redirect("/")
    
    



if __name__ == "__main__":
    app.run(debug=True)