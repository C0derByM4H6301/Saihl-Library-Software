import sqlite3

def create_database():
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            isbn TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_book(title, author, year, isbn):
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def search_book(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = c.fetchall()
    conn.close()
    return rows

def delete_book(id):
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update_book(id, title, author, year, isbn):
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()
