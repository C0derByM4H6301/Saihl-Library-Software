import sqlite3
import csv

def connect():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            student TEXT,
            number INTEGER,
            date TEXT
        );
    ''')
    conn.commit()
    conn.close()

def add_book(title, author, student, number, date):
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?,?)",(title, author, student, number, date))
    conn.commit()
    conn.close()

def delete_book(id):
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()

def edit_book(id, title="", author="", student="", number="", date=""):
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, student=?, number=?, date=? WHERE id=?",
                (title, author, student, number, date, id))
    conn.commit()
    conn.close()

def show_books():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

def export_csv():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()

    with open('library.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Title', 'Author', 'Student', 'Number', 'Date'])
        writer.writerows(rows)

def import_csv():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM books')
    with open('library.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'ID':
                continue
            cur.execute("INSERT INTO books VALUES (?,?,?,?,?,?)", (row[0], row[1], row[2], row[3], row[4], row[5]))
    conn.commit()
    conn.close()
