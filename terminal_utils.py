import os
import sys
import time

def clear_terminal():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    """Pauses the program until the user presses Enter."""
    input("Press Enter to continue...")
