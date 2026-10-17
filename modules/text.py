from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def show_message(message_path: Path):
    if not message_path.exists():
        console.print(
            "[bold red]Error:[/bold red] Message file not found."
        )
        return

    message = message_path.read_text(encoding="utf-8")

    console.clear()

    console.print(
        Panel(
            Text(message, style="white"),
            title="[bold bright_magenta]СООБЩЕНИЕ[/bold bright_magenta]",
            subtitle="[dim]От твоего сына[/dim]",
            border_style="bright_magenta",
            padding=(1, 2),
        )
    )
