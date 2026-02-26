import sqlite3

def create_connection():
    return sqlite3.connect("database.db")  # убедись, что имя совпадает с твоей базой

def get_books_by_author(author):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT name FROM books WHERE author = ? ORDER BY name ASC"
    cursor.execute(query, (author,))
    books = [row[0] for row in cursor.fetchall()]
    conn.close()
    return books

if __name__ == "__main__":
    author_name = "Лев Толстой"
    books_list = get_books_by_author(author_name)
    print(f"Книги автора {author_name}: {books_list}")