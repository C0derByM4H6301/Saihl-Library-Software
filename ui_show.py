from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.align import Align

def show_gui():
    layout = Layout(name="root")

    with layout:
        with layout.split_column():
            console = Console()
            console.print(Panel("[bold green]List of all records[/bold green]"))
            table = Table(title="Records")
            table.add_column("ID", justify="center", style="cyan")
            table.add_column("Name", justify="center", style="magenta")
            table.add_column("School Code", justify="center", style="green")
            table.add_column("Book", justify="center", style="blue")
            table.add_column("Author", justify="center", style="yellow")
            table.add_column("Borrowed Date", justify="center", style="red")
            table.add_column("Return Date", justify="center", style="white")
            console.print(Align.center(table))

    return layout

