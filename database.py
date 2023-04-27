# https://github.com/C0derByM4H6301/Saihl-Library-Software
import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS library (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                school_code TEXT NOT NULL,
                book TEXT NOT NULL,
                author TEXT NOT NULL,
                borrowed_date TEXT NOT NULL,
                due_date TEXT NOT NULL
            );
        """)
        self.connection.commit()

    def add_book(self, name, school_code, book, author, borrowed_date, due_date):
        self.cursor.execute("""
            INSERT INTO library(name, school_code, book, author, borrowed_date, due_date) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, school_code, book, author, borrowed_date, due_date))
        self.connection.commit()

    def remove_book(self, id):
        self.cursor.execute("""
            DELETE FROM library WHERE id = ?
        """, (id,))
        self.connection.commit()

    def get_overdue_books(self):
        self.cursor.execute("""
            SELECT * FROM library WHERE due_date < CURRENT_DATE;
        """)
        return self.cursor.fetchall()
