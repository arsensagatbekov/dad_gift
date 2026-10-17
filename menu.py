from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from modules.image import show_image
from modules.text import show_message
from modules.music import play_music
from modules.episode import show_episode
from modules.secret import show_secret
console = Console()
ASSETS = Path(__file__).parent / "assets"
def clear_screen():
    """Clear the terminal screen."""
    console.clear()
def display_menu():
    """Display the main menu."""
    clear_screen()
    title = Text()
    title.append("DAD", style="bold bright_green")
    title.append("_OS", style="bold white")
    title.append(" v1.0", style="dim green")
    subtitle = Text(
        "DAY OF THE YEAR EDITION",
        style="green",
        justify="center",
    )
    menu_items = Text()
    menu_items.append("\n")
    menu_items.append("  [i] ", style="bold bright_green")
    menu_items.append("IMAGE", style="bold white")
    menu_items.append("       Уменьши размер шрифта до минимума\n", style="dim")
    
    menu_items.append("  [t] ", style="bold bright_green")
    menu_items.append("TEXT", style="bold white")
    menu_items.append("        Душевные слова\n", style="dim")
    
    menu_items.append("  [m] ", style="bold bright_green")
    menu_items.append("MUSIC", style="bold white")
    menu_items.append("       Секретная мелодия\n", style="dim")
    
    menu_items.append("  [e] ", style="bold bright_green")
    menu_items.append("EPISODE", style="bold white")
    menu_items.append("     Давным-давно...\n", style="dim")
    
    menu_items.append("  [q] ", style="bold bright_green")
    menu_items.append("QUIT", style="bold white")
    menu_items.append("        Ну ты это, заходи, если что...\n", style="dim")
    
    menu_items.append("\n")
    menu_items.append(" СТАТУС СИСТЕМЫ: ", style="dim")
    menu_items.append("ONLINE", style="bold bright_green")
    menu_items.append("\n\n")
    panel_content = Text()
    panel_content.append(title)
    panel_content.append("\n")
    panel_content.append(subtitle)
    panel_content.append("\n")
    panel_content.append(menu_items)
    panel = Panel(
        Align.center(panel_content),
        border_style="green",
        padding=(1, 4),
        title="[bold green]root@dad[/bold green]",
        subtitle="[dim green]Birthday Protocol[/dim green]",
    )
    console.print()
    console.print(Align.center(panel))
    console.print()
    console.print(
        "[dim]Сделай свой выбор...[/dim]"
    )
def placeholder(section_name):
    """Display a temporary placeholder for unfinished sections."""
    console.print()
    console.print(
        Panel(
            f"[bold bright_green]{section_name}[/bold bright_green]\n\n"
            "[dim]This module is not implemented yet.[/dim]",
            border_style="green",
            title="[dim]SYSTEM MESSAGE[/dim]",
        )
    )
    console.input(
        "\n[dim]Нажмите ENTER, чтобы вернуться в главное меню[/dim]"
    )
def run_menu():
    """Main menu loop."""
    while True:
        display_menu()
        choice = console.input(
            "[bold bright_green]root@dad:~$ [/bold bright_green]"
        ).strip().lower()
        if choice == "i":
            show_image(ASSETS / "portrait.txt")
        elif choice == "t":
            show_message(ASSETS / "message.txt")
        elif choice == "m":
            play_music(ASSETS / "birthday.mp3")
        elif choice == "e":
            show_episode()
        elif choice == "s":
            show_secret()
        elif choice in ("q", "quit", "exit"):
            console.print(
                "\n[bold green]Отключение Dad_OS...[/bold green]"
            )
            console.print("[dim]Хорошего дня рождения![/dim]\n")
            break
        else:
            console.print(
                "\n[bold red]ERROR:[/bold red] "
                "[dim]Такого действия не придумал[/dim]"
            )
            console.input("[dim]Нажмите ENTER, чтобы продолжить...[/dim]")
            continue
        # Return to the menu after a module finishes.
        if choice not in ("q", "quit", "exit"):
            console.input(
                "\n[dim]Нажмите ENTER, чтобы вернуться в главное меню[/dim]"
            )
if __name__ == "__main__":
    try:
        run_menu()
    except (KeyboardInterrupt, EOFError):
        console.print("\n[dim green]Session terminated.[/dim green]")