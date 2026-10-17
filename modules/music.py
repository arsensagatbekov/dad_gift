from pathlib import Path
import shutil
import subprocess

from rich.console import Console

console = Console()


def play_music(audio_path: Path):
    if not audio_path.exists():
        console.print(
            "[bold red]Error:[/bold red] Файл не найден."
        )
        return

    player = shutil.which("mpv")

    if player is None:
        console.print(
            "[bold red]Error:[/bold red] mpv is not installed."
        )
        console.print("Install it with: sudo apt install mpv")
        return

    console.print("[bold green]Проигрываем песенку...[/bold green]")

    try:
        subprocess.run(
            [player, "--no-video", str(audio_path)],
            check=False,
        )
    except OSError as error:
        console.print(f"[bold red]Ошибка проигрывания:[/bold red] {error}")
