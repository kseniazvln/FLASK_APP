import sqlite3

DB_PATH = './todo.db'  # Путь к бд
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'


# добавление элемента
def add_to_list(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        # Как только соединение установлено, мы используем объект cursor для выполнения запросов
        c = conn.cursor()
        # Сохраняйте начальный статус как не запущенный
        c.execute('insert into items(item, status) values(?,?)', (item, NOTSTARTED))
        # Сохраняем изменения
        conn.commit()
        return {"item": item, "status": NOTSTARTED}
    except Exception as e:
        print('Error: ', e)
        return None


# вывод всех элементов
def get_all_items():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('select * from items')
        rows = c.fetchall()
        return {"count": len(rows), "items": rows}
    except Exception as e:
        print('Error: ', e)
        return None

def delete_item(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('delete from items where item=?', (item,))
        conn.commit()
        return {'item': item}
    except Exception as e:
        print('Error: ', e)
        return None