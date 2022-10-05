import sqlite3 as sq

from django import db
from models import Item, Category

db_name = "tdb.db"

# Функция для создания нужной таблицы





# Получение полного списка объектов из БД
def get_items():
    with sq.connect(db_name) as con:
        cur = con.cursor()
        cur.execute("""
        SELECT id, name, category FROM items
        """)
        raw_data = cur.fetchall()
        items = []
        for i in raw_data:
            items.append(Item(i[0], i[1], i[2]))
        return items


# Редактирование записи в БД
def update_item(id, name, category):
    with sq.connect(db_name) as con:
        cur = con.cursor()
        cur.execute(f"UPDATE items SET name = '{name}', category = '{category}'  WHERE id = {id}")


# Добавление новой записи
def add_item(item):
    with sq.connect(db_name) as con:
        cur = con.cursor()
        cur.execute(f"INSERT INTO items(name, category) VALUES ('{item.name}', '{item.category}')")


# Удаление записи из БД
def delete_item(id):
    with sq.connect(db_name) as con:
        cur = con.cursor()
        cur.execute(f"DELETE FROM items WHERE id={id}")


# Получение категорий
def get_categories():
    with sq.connect(db_name) as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM categories""")
        categories = []
        raw_data = cur.fetchall()
        for i in raw_data:
            categories.append(Category(i[0], i[1]))
        return categories


# Добавление категории
def add_category(name):
    with sq.connect(db_name) as con:
        cur = con.cursor()
        cur.execute(f"INSERT INTO categories(name) VALUES ('{name}')")


# Удаление категории
def delete_category(id):
    with sq.connect(db_name) as con:
        cur = con.cursor()
        cur.execute(f"DELETE FROM categories WHERE id={id}")


# Редактирование категории
def update_category(id, name):
    with sq.connect(db_name) as con:
        cur = con.cursor()
        cur.execute(f"UPDATE categories SET name = '{name}' WHERE id = {id}")


