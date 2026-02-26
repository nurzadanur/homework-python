import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.cursor()

# Удаляем таблицу students, если она есть
cursor.execute("DROP TABLE IF EXISTS students")

connection.commit()
connection.close()
print("Таблица students удалена")