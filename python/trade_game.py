# This program serves to execute the main gameplay loop of the text-based implementation of the Trade game.

import flavor
import network
import planet
import ui
import platform

def parse_input(input_string : str, board : list[list[bool]], planet_list : list[planet.Planet]) -> None:
    """
    parse_input(...) takes user input and decides what to do with it.
    """
    match input_string.split():
        case ["b"] | ["board"]:
            ui.show_board(board, planet_list)

        case ["info", planet_id_string]:
            ui.show_planet(planet_list, planet_id_string)

        case ["h"] | ["help"]:
            ui.action_prompt()

        case ["p"] | ["probe"]:
            found_planets = [planet.Planet() for i in range(3)]
            new_planet = ui.probe_prompt(found_planets)
            if new_planet != None:
                network.add_planet(planet_list, board, new_planet)

        case ["trade", planet_1_id_string, planet_2_id_string]:
            # p1_id, p2_id = ui.trade_prompt()
            planet_1_id = int(planet_1_id_string)
            planet_2_id = int(planet_2_id_string)

            planet_1 = planet_list[planet_1_id]
            planet_2 = planet_list[planet_2_id]
            
            network.trade(board, planet_1, planet_2)
        case ["QUIT"]:
            return
        case _:
            print("Please enter a valid action")

def main() -> None:
    """
    main() is the main gameplay loop including initialization of game board and planet list.
    """
    ui.splash()

    mode = ui.choose_mode()
    if mode == "y" or mode == "yes":
        flavor.show_flavor()
    
    ui.get_seed_prompt()

    planet_list = []
    board = []
    
    # start with one planet
    network.add_planet(planet_list, board, planet.Planet())

    print()
    print("You begin with a single planet.")
    planet_list[0].summary()
    
    action = "dummy"
    while action != "QUIT":
        ui.action_prompt()
        action = input()
        parse_input(action, board, planet_list)

if __name__ == '__main__':
    # pattern matching was introduced in version 3.10
    if platform.python_version() >= '3.10':
        main()
    else:
        print("""This program is only able to be run on 
              python versions greater than or equal to 3.10.""")