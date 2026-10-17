from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def show_image(image_path: Path):
    if not image_path.exists():
        console.print(
            "[bold red]Error:[/bold red] Portrait file not found."
        )
        return

    content = image_path.read_text(encoding="utf-8")

    console.clear()

    # Text.from_ansi preserves ANSI terminal colors if the file uses them.
    portrait = Text.from_ansi(content)

    console.print(
        Panel(
            portrait,
            title="[bold green]CLASSIFIED: DAD[/bold green]",
            border_style="green",
            padding=(0, 1),
        )
    )
