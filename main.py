import map
import player
import boss
import deck
import water_factory
import wind_factory
import grass_factory
import battle 


def main():

    print(" Welcome to Inscription Game\n Are you worthy to defeat the Boss")
    name = input("What is your name, player? ")
    player_1 = player.Player(name)


    Game_map = map.Map()
    quit = False 


    while not quit:
        print(Game_map.show_map(player_1.location))
        print("1. Go stright\n2. Go left\n3. Go right\n4. Quit")
        menu_choice = input("Enter choice: ")

        move = ''
        if menu_choice == "1":
            move = player_1.go_forward()
        elif menu_choice == "2":
            move = player_1.go_left()
        elif menu_choice == "3":
            move = player_1.go_right()

        elif menu_choice == "4":
            quit = True 

        if move == 'I':
            player_1.shopItem()
        elif move == 'U':
            player_1.displayDeck()
            player_1._deck.upgrade(player_1._deck._cards[0])
        if move == 'B':
            print("Battle")
            battle.battle(player_1, boss_1)
            
        print()
            




main()