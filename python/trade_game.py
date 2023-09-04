# This program serves to execute the main gameplay loop of the text-based implementation of the Trade game.

import flavor
import network
import planet
import ui

def parse_input(input_string, board, planet_list):
    match input_string:
        case "b" | "board":
            ui.show_board(board, planet_list)

        case "i" | "info":
            ui.show_planet(planet_list)

        case "h" | "help":
            ui.action_prompt()

        case "p" | "probe":
            found_planets = [planet.Planet() for i in range(3)]
            new_planet = ui.probe_prompt(found_planets)
            if new_planet != None:
                network.add_planet(planet_list, board, new_planet)

        case "t" | "trade":
            p1_id, p2_id = ui.trade_prompt()
            network.trade(board, planet_list[int(p1_id)], planet_list[int(p2_id)])
        case "QUIT":
            return
        case _:
            print("Please enter a valid action")

def main():
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
    main()