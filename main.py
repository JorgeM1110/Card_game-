import map
import player
import battle 
import deck
import check_input
from terminal_utils import clear_terminal, pause
from boss_file import boss

def welcome_message(name):
    print("\noOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoO\n")
    print(f"Welcome to AquaScrypt {name}! \n")
    print("Will you make it back to the surface with undiscovered treasures?")
    print(f"Well {name}, good luck diving...\n")
    print("oOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoOoO\n")

def main():
    clear_terminal()
    name = input("What is your name, diver? ")
    welcome_message(name)

    hero = player.Player(name)
    villain = boss.Boss("Jeff")
    game_map = map.Map()

    pause()
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
            hero.display_deck()
            hero._deck.upgrade(hero._deck._cards[0])
        elif move == 'B':
            battle.battle(hero, villain)
        elif move == 'A':
            hero._deck.sacrifice()
        
        print()
main()