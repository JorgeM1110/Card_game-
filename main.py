import map
import player
import battle 
import deck
import check_input
from terminal_utils import clear_terminal, pause, delay_print, delay_input, delay
from boss_file import boss

def welcome_message(name):
    
    delay_print(f"\nWelcome to AquaScrypt {name}! \n")
    delay_print("Will you make it back to the surface with undiscovered treasures?...")
    delay_print("or will the sea consume you...")
    delay(1.5)
    delay_print(f"\nWell {name}, good luck diving!\n")

def main():
    clear_terminal()
    # delay_print("What is your name, diver? ")
    # name = input("Name: ")
    # welcome_message(name)
    
    name = "Joe"

    hero = player.Player(name)
    villian = boss.Boss("Jeff")
    game_map = map.Map()

    # pause()
    clear_terminal()
    
    quit = False 
    while not quit :
        print(game_map.show_map(hero.location))
        print("1. Go stright\n2. Go left\n3. Go right\n4. Quit")
        menu_choice = input("Enter choice: ")

        move = ''
        if menu_choice == "1":
            move = hero.go_forward()
        elif menu_choice == "2":
            move = hero.go_left()
        elif menu_choice == "3":
            move = hero.go_right()
        elif menu_choice == "4":
            quit = True 

        clear_terminal()

        if move == 'I':
            hero.shop_item()
        elif move == 'U':
            clear_terminal()
            hero._deck.upgrade()
        elif move == 'B':
            battle.battle(hero, villian)
        elif move == 'A':
            hero._deck.sacrifice()
        
        print()
main()