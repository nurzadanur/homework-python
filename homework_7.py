import sqlite3

def create_connection():
    return sqlite3.connect("database.db")


def create_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)

    connection.commit()
    connection.close()


def insert_books():
    connection = create_connection()
    cursor = connection.cursor()


    cursor.execute("DELETE FROM books")

    books = [
        ("Война и мир", "Лев Толстой", 1869, "Роман", 1225, 3),
        ("Преступление и наказание", "Фёдор Достоевский", 1866, "Философский роман", 671, 4),
        ("Мастер и Маргарита", "Михаил Булгаков", 1967, "Мистика", 480, 5),
        ("Анна Каренина", "Лев Толстой", 1877, "Роман", 864, 2),
        ("Евгений Онегин", "Александр Пушкин", 1833, "Поэма", 224, 6),
        ("Отцы и дети", "Иван Тургенев", 1862, "Роман", 352, 3),
        ("Герой нашего времени", "Михаил Лермонтов", 1840, "Роман", 256, 4),
        ("Доктор Живаго", "Борис Пастернак", 1957, "Роман", 592, 2),
        ("Тихий Дон", "Михаил Шолохов", 1940, "Исторический роман", 1024, 3),
        ("Белая гвардия", "Михаил Булгаков", 1925, "Исторический роман", 384, 5)
    ]

    cursor.executemany("""
        INSERT INTO books (
            name,
            author,
            publication_year,
            genre,
            number_of_pages,
            number_of_copies
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_table()
    insert_books()
    print("Таблица создана и книги успешно добавлены.")