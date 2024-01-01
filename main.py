import map
import player
import battle 
import deck
from boss_file import boss
from factories import water_factory, wind_factory, grass_factory



def main():

    print("Welcome to Inscription Game\nAre you worthy to defeat the Boss")
    name = input("What is your name, hero? ")
    hero = player.Player(name)
    villain = boss.Boss("AEYBGF")

    Game_map = map.Map()
    quit = False 


    while not quit:
        print(Game_map.show_map(hero.location))
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

        if move == 'I':
            hero.shop_item()
        elif move == 'U':
            hero.display_deck()
            hero._deck.upgrade(hero._deck._cards[0])
        if move == 'B':
            print("Battle")
            battle.battle(hero, villain)

        elif move == 'A':
            hero._deck.sacrifice()
        

            
        print()
            




main()