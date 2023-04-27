# https://github.com/C0derByM4H6301/Saihl-Library-Software
import argparse
from ui import *

parser = argparse.ArgumentParser(description="Library Management System")

parser.add_argument("command", choices=["show", "add", "remove", "check"], help="Command to execute")

parser.add_argument("--id", help="ID of the book to remove", type=int)

args = parser.parse_args()

if args.command == "show":
    show_books()
elif args.command == "add":
    add_book()
elif args.command == "remove":
    if not args.id:
        print("Please specify ID of book to remove with --id option.")
    else:
        remove_book(args.id)
elif args.command == "check":
    check_books()
