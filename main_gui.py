import tkinter as tk
from tkinter import ttk
from ui_add import AddUI
from ui_remove import RemoveUI
from ui_show import ShowUI
from ui_check import CheckUI


class MainUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Library Management System for Saihl")
        self.geometry("500x300")

        # create notebook widget
        notebook = ttk.Notebook(self)

        # create tabs
        add_tab = ttk.Frame(notebook)
        remove_tab = ttk.Frame(notebook)
        show_tab = ttk.Frame(notebook)
        check_tab = ttk.Frame(notebook)

        # add tabs to notebook
        notebook.add(add_tab, text="Add")
        notebook.add(remove_tab, text="Remove")
        notebook.add(show_tab, text="Show")
        notebook.add(check_tab, text="Check")

        # create ui objects for each tab
        add_ui = AddUI(add_tab)
        remove_ui = RemoveUI(remove_tab)
        show_ui = ShowUI(show_tab)
        check_ui = CheckUI(check_tab)

        # pack notebook widget
        notebook.pack(expand=True, fill="both")


if __name__ == "__main__":
    app = MainUI()
    app.mainloop()

