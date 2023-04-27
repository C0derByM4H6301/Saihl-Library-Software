import csv
import datetime

class Library:
    def __init__(self, filename):
        self.filename = filename
        
    def show_books(self):
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            books = []
            for row in reader:
                books.append(row)
        return books
    
    def add_book(self, name, author, student_name, student_surname, student_number):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, author, student_name, student_surname, student_number, datetime.datetime.now()])
            
    def remove_book(self, name):
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            books = []
            for row in reader:
                if row[0] != name:
                    books.append(row)
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(books)
            
    def edit_book(self, name, column, value):
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            books = []
            for row in reader:
                if row[0] == name:
                    row[column] = value
                books.append(row)
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(books)
