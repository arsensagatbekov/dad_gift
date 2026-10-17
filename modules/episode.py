import random
import time
import shutil

from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.live import Live
from rich.console import Group
from rich.panel import Panel
from rich.style import Style

console = Console()

# Change the episode title here.
EPISODE_TITLE = "ЭПИЗОД XLVII"

EPISODE_SUBTITLE = "ЛУЧШИЙ ОТЕЦ"

# Edit the story to make it personal.
STORY = """
Настал период поздравлений

По всей галактике отмечают,
Как легендарный отец преодолел очередной год
Приключений, трудностей и опасностей.

Мастер слога и технологий,
Настоящий иследователь и герой
Для тех, кому посчасливелось его встретить

Его знания необъемлемы,
Его доброта бесконечна
Его шутки не оставят никого равнодушным.

Пусть дела идут гладко, а баги не встречают тебя
Пусть сердце твое семья радует
И пусть музыка никогда не угасает

И да пребудет с тобой Сила...

Всегда.
"""


def generate_stars(width, height, count=70):
    """Generate random star positions."""
    stars = []

    for _ in range(count):
        stars.append(
            (
                random.randint(0, max(0, width - 1)),
                random.randint(0, max(0, height - 1)),
            )
        )

    return stars


def make_starfield(width, height, stars):
    """Create a simple starfield."""
    canvas = [
        [" " for _ in range(width)]
        for _ in range(height)
    ]

    for x, y in stars:
        if 0 <= x < width and 0 <= y < height:
            canvas[y][x] = random.choice([".", ".", ".", "*"])

    return "\n".join("".join(row) for row in canvas)


def show_episode():
    """Display a Star Wars-inspired birthday crawl."""

    console.clear()

    console.print(
        Panel(
            Align.center(
                "[bold yellow]ДАВНЫМ-ДАВНО, В ДАЛЕКОЙ-ДАЛЕКОЙ ГАЛАКТИКЕ...[/bold yellow]"
            ),
            border_style="yellow",
        )
    )

    time.sleep(3)

    width = min(shutil.get_terminal_size().columns, 100)
    height = min(shutil.get_terminal_size().lines - 4, 30)

    stars = generate_stars(width, height)

    title = Text(
        f"\n{EPISODE_TITLE}\n\n{EPISODE_SUBTITLE}\n",
        style=Style(color="yellow", bold=True),
        justify="center",
    )

    console.clear()
    console.print(Align.center(title))

    time.sleep(3)

    story_lines = STORY.strip().splitlines()

    # Add blank lines to create space before the text enters.
    crawl_lines = [""] * height + story_lines + [""] * height

    try:
        with Live(console=console, refresh_per_second=60) as live:
            for offset in range(len(crawl_lines)):
                starfield = make_starfield(width, height, stars)
                star_rows = starfield.splitlines()

                visible_lines = crawl_lines[offset:offset + height]

                frame_lines = []

                for row in range(height):
                    star_line = star_rows[row] if row < len(star_rows) else ""
                    story_line = (
                        visible_lines[row]
                        if row < len(visible_lines)
                        else ""
                    )

                    line = Text(star_line, style="dim white")

                    if story_line.strip():
                        line.append("\n")
                        line.append(story_line, style="bold yellow")

                    frame_lines.append(line)

                frame = Group(
                    *[
                        Align.center(line, width=width)
                        for line in frame_lines
                    ]
                )

                live.update(
                    Panel(
                        frame,
                        border_style="blue",
                        title="[bold yellow]DAD_OS // ЭПИЗОД[/bold yellow]",
                        width=width + 4,
                    )
                )
                
                time.sleep(0.4)


    except KeyboardInterrupt:
        pass

    console.clear()

    console.print(
        Panel(
            Align.center(
                "[bold yellow]Да пребудет с тобой Сила[/bold yellow]\n\n"
                "[dim]Конец.[/dim]"
            ),
            border_style="yellow",
        )
    )
