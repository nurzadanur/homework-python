import sqlite3

def get_books_by_author(author):
    conn = sqlite3.connect("your_database.db")
    cursor = conn.cursor()
    query = "SELECT title FROM books WHERE author = ? ORDER BY title ASC"
    cursor.execute(query, (author,))
    books = [row[0] for row in cursor.fetchall()]
    conn.close()
    return books

author_name = "J.K. Rowling"
books_list = get_books_by_author(author_name)
print(books_list)