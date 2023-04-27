# https://github.com/C0derByM4H6301/Saihl-Library-Software
from rich.console import Console
from rich.table import Table
from datetime import date
from database import Database

console = Console()
db = Database("library.db")

def show_books():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim")
    table.add_column("Name")
    table.add_column("School Code")
    table.add_column("Book")
    table.add_column("Author")
    table.add_column("Borrowed Date")
    table.add_column("Due Date")

    for book in db.cursor.execute("SELECT * FROM library"):
        table.add_row(str(book[0]), book[1], book[2], book[3], book[4], book[5], book[6])

    console.print(table)

def remove_book(id):
    db.remove_book(id)
    console.print(f"Book with ID {id} removed.")

def add_book():
    name = input("Enter student name: ")
    while not name:
        name = input("Please enter student name: ")
    school_code = input("Enter school code: ")
    while not school_code:
        school_code = input("Please enter school code: ")
    book = input("Enter book name: ")
    while not book:
        book = input("Please enter book name: ")
    author = input("Enter author name: ")
    while not author:
        author = input("Please enter author name: ")
    borrowed_date = input("Enter borrowed date (YYYY-MM-DD): ")
    while not borrowed_date:
        borrowed_date = input("Please enter borrowed date (YYYY-MM-DD): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    while not due_date:
        due_date = input("Please enter due date (YYYY-MM-DD): ")
    db.add_book(name, school_code, book, author, borrowed_date, due_date)
    console.print("Book added successfully.")

def check_books():
    books = db.get_overdue_books()
    if not books:
        console.print("No books overdue.")
        return
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim")
    table.add_column("Name")
    table.add_column("School Code")
    table.add_column("Book")
    table.add_column("Author")
    table.add_column("Borrowed Date")
    table.add_column("Due Date")

    for book in books:
        table.add_row(str(book[0]), book[1], book[2], book[3], book[4], book[5], book[6])

    console.print(table)
