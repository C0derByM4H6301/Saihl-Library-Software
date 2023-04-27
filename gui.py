# https://github.com/C0derByM4H6301/Saihl-Library-Software
import tkinter as tk
import os

class LibraryManagementSystem:
    def __init__(self, master):
        self.master = master
        master.title("Şanlıurfa Anadolu İmam Hatip Kütüphane Yönetim Sistemi")

        self.label = tk.Label(master, text="Kütüphane Yönetim Sistemi")
        self.label.pack()

        self.show_button = tk.Button(master, text="Kitapları Listele", command=self.show_books)
        self.show_button.pack()

        self.add_button = tk.Button(master, text="Kitap Ekle", command=self.add_book)
        self.add_button.pack()

        self.remove_button = tk.Button(master, text="Kitap Sil", command=self.remove_book)
        self.remove_button.pack()

        self.check_button = tk.Button(master, text="Geçikenleri Kontrol Et", command=self.check_overdue)
        self.check_button.pack()

    def show_books(self):
        os.system('python main.py show')

    def add_book(self):
        os.system('python main.py add')

    def remove_book(self):
        os.system('python main.py remove --id')

    def check_overdue(self):
        os.system('python main.py check')

root = tk.Tk()
my_gui = LibraryManagementSystem(root)
root.mainloop()
