from tkinter import *
from tkinter import messagebox
from database import add_book

class AddBookUI:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Add Book")

        Label(parent, text="Student Name:").grid(row=0, column=0, sticky=W)
        Label(parent, text="School Code:").grid(row=1, column=0, sticky=W)
        Label(parent, text="Book Name:").grid(row=2, column=0, sticky=W)
        Label(parent, text="Author:").grid(row=3, column=0, sticky=W)
        Label(parent, text="Issue Date:").grid(row=4, column=0, sticky=W)
        Label(parent, text="Due Date:").grid(row=5, column=0, sticky=W)

        self.student_name_entry = Entry(parent)
        self.school_code_entry = Entry(parent)
        self.book_name_entry = Entry(parent)
        self.author_entry = Entry(parent)
        self.issue_date_entry = Entry(parent)
        self.due_date_entry = Entry(parent)

        self.student_name_entry.grid(row=0, column=1)
        self.school_code_entry.grid(row=1, column=1)
        self.book_name_entry.grid(row=2, column=1)
        self.author_entry.grid(row=3, column=1)
        self.issue_date_entry.grid(row=4, column=1)
        self.due_date_entry.grid(row=5, column=1)

        add_book_button = Button(parent, text="Add Book", command=self.add_book)
        add_book_button.grid(row=6, column=0, columnspan=2)

    def add_book(self):
        student_name = self.student_name_entry.get()
        school_code = self.school_code_entry.get()
        book_name = self.book_name_entry.get()
        author = self.author_entry.get()
        issue_date = self.issue_date_entry.get()
        due_date = self.due_date_entry.get()

        if not all([student_name, school_code, book_name, author, issue_date, due_date]):
            messagebox.showerror("Error", "Please fill in all fields")
        else:
            add_book(student_name, school_code, book_name, author, issue_date, due_date)
            messagebox.showinfo("Success", "Book added successfully")

