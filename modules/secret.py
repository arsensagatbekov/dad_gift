import shutil
import subprocess
import time
from pathlib import Path
from getpass import getpass

from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text

console = Console()

BASE_DIR = Path(__file__).resolve().parent.parent
VIDEO_PATH = BASE_DIR / "assets" / ".secret_video.avi"

PASSWORD = "orapas"


def show_secret_intro():
    console.clear()

    title = Text()
    title.append("DAD", style="bold bright_green")
    title.append("_OS", style="bold white")

    subtitle = Text(
        "\nСЕКРЕТНЫЙ АРХИВ ВОСПОМИНАНИЙ\n",
        style="bold yellow",
        justify="center",
    )

    content = Text()
    content.append("\nТРЕБУЕТСЯ АВТОРИЗАЦИЯ\n\n", style="bold red")
    content.append("Обнаружено засекреченное воспоминание.\n", style="white")
    content.append("Доступ разрешён только избранному.\n", style="dim")

    console.print()
    console.print(
        Align.center(
            Panel(
                Align.center(
                    Text.assemble(title, "\n", subtitle, content)
                ),
                border_style="bright_green",
                title="[bold green]root@dad:~[/bold green]",
                subtitle="[dim]СОВЕРШЕННО СЕКРЕТНО[/dim]",
                padding=(1, 4),
            )
        )
    )


def play_access_animation():
    messages = [
        "Подключение к архиву воспоминаний...",
        "Проверка прав доступа...",
        "Расшифровка воспоминаний детства...",
        "Восстановление видеозаписи...",
        "ДОСТУП РАЗРЕШЁН",
    ]

    console.print()

    with Progress(
        SpinnerColumn(),
        TextColumn("{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("", total=len(messages))

        for message in messages:
            progress.update(task, description=message)
            time.sleep(0.8)
            progress.advance(task)


def play_video():
    player = shutil.which("mpv")

    if not player:
        console.print(
            "\n[bold red]ОШИБКА:[/bold red] Видеоплеер mpv не установлен."
        )
        console.print(
            "Установи его командой: [green]brew install mpv[/green]"
        )
        return

    if not VIDEO_PATH.exists():
        console.print(
            f"\n[bold red]ОШИБКА:[/bold red] Видео не найдено:\n{VIDEO_PATH}"
        )
        return

    console.clear()
    console.print(
        Align.center(
            Panel(
                "[bold yellow]ВОСПОМИНАНИЕ ИЗ ПРОШЛОГО[/bold yellow]\n\n"
                "[white]Некоторые моменты заслуживают вечной жизни.[/white]\n"
                "[dim]Подготовка архивной видеозаписи...[/dim]",
                border_style="yellow",
                padding=(2, 5),
            )
        )
    )

    time.sleep(2)

    try:
        subprocess.run(
            [player, "--", str(VIDEO_PATH)],
            check=False,
        )
    except OSError as error:
        console.print(f"\n[red]Не удалось запустить видео: {error}[/red]")


def show_secret():
    show_secret_intro()

    for attempt in range(3):
        password = getpass("\n🔐 Введи пароль: ")

        if password == PASSWORD:
            console.print(
                "\n[bold bright_green]ДОСТУП РАЗРЕШЁН[/bold bright_green]"
            )
            time.sleep(1)

            play_access_animation()
            time.sleep(1)

            play_video()
            return

        console.print("\n[bold red]ДОСТУП ЗАПРЕЩЁН[/bold red]")
        remaining = 2 - attempt

        if remaining > 1:
            console.print(f"[dim]Ты знаешь пароль 😉[/dim]")
        if remaining > 0:
            if remaining < 1:
                console.print(f"[dim]Подсказка: одно слово, с маленькой буквы[/dim]")
            console.print(f"[dim]Осталось попыток: {remaining}[/dim]")

        time.sleep(1)

    console.print("\n[bold red]АРХИВ ЗАБЛОКИРОВАН[/bold red]")


if __name__ == "__main__":
    show_secret()