import time

from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.live import Live

console = Console()

BANNER = r"""
   ,-.
   | |
   | "--.  ,--.-.,-.--. ,-.--. ,-. ,-.
   | ,-. \/ ,-. || ,-. \| ,-. \| | | |
   | | | |\ `-' || `-' /| `-' /| `-' |
   `-' `-' `--'-'| .--' | .--'  `--. |
                 | |    | |        | |
                 `-'    `-'        `-'
,-.     _       ,-.  ,-.        ,-.
| |    (_)      | |_ | |        | |
| "--. ,-.,-.--.|  _)| "--.  ,--" | ,--.-.,-. ,-.
| ,-. \| || ,-./| |  | ,-. \/ ,-. |/ ,-. || | | |
| `-' /| || |   | |  | | | |\ `-' |\ `-' || `-' |
"-'--' `-'`-'   `-'  `-' `-' `--'-' `--'-' `--. |
                                              | |
                                              `-'
"""


def play_intro():
    console.clear()

    console.print(
        Panel(
            Align.center("[bold green]INITIALIZING BIRTHDAY PROTOCOL...[/bold green]"),
            border_style="green",
        )
    )

    time.sleep(1)

    lines = BANNER.splitlines()
    max_width = max(len(line) for line in lines)

    # Reveal the banner from left to right.
    with Live(
        console=console,
        refresh_per_second=30,
        transient=True,
    ) as live:
        for width in range(max_width + 1):
            visible_lines = []

            for line in lines:
                visible_lines.append(
                    Text(line[:width], style="bold green")
                )

            content = Text("\n").join(visible_lines)

            live.update(
                Panel(
                    Align.center(content),
                    border_style="green",
                    title="[bold green]SYSTEM BOOT[/bold green]",
                )
            )

            time.sleep(.03)

    console.print()
    console.print(
        Align.center(
            "[bold bright_green]ДОБРО ПОЖАЛОВАТЬ в ОС для Вас, АРМАН! [/bold bright_green]"
        )
    )
    console.print()

    console.input("[bold green]Пожалуйста, нажмите на ENTER, чтобы продолжить...[/bold green]")
    console.clear()
