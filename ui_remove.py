from rich.layout import Layout
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt

def remove_gui():
    layout = Layout(name="root")

    with layout:
        with layout.split_column():
            console = Console()
            console.print(Panel("[bold green]Remove a record[/bold green]"))
            id = Prompt.ask("Enter the ID of the record you want to remove", default="", validate=bool)
            console.print(f"ID to remove: {id}")

    return layout

