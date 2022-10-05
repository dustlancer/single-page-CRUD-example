import sqlite3 as sq
from models import Item

db_name = "tdb.db"

# Функция для создания нужной таблицы
'''with sq.connect("") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )""")'''


# Получение полного списка объектов из БД
def get_items():
    with sq.connect(db_name) as con:
        cur = con.cursor()
        cur.execute("""
        SELECT id, name FROM items
        """)
        raw_data = cur.fetchall()
        items = []
        for i in raw_data:
            items.append(Item(i[0], i[1]))
        return items


# Редактирование записи в БД
def update_item(id, name):
    with sq.connect(db_name) as con:
        cur = con.cursor()
        cur.execute(f"UPDATE items SET name = '{name}' WHERE id = {id}")


# Добавление новой записи
def add_item(item):
    with sq.connect(db_name) as con:
        cur = con.cursor()
        cur.execute(f"INSERT INTO items(name) VALUES ('{item.name}')")

# Удаление записи из БД
def delete_item(id):
    with sq.connect(db_name) as con:
        cur = con.cursor()
        cur.execute(f"DELETE FROM items WHERE id={id}")


