from modules.intro import play_intro
from menu import run_menu
def main():
    play_intro()
    run_menu()
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nХорошего дня!")
