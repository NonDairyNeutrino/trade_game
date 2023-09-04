# interface for the user to interact with the program

import random as rng
import time
from planet import Planet

# TODO: add docstrings to everything

# splash banner that displays when you open the game
def splash():
    banner = """
    =====================
            TRADE        
    =====================
    """
    welcome = "Welcome to TRADE; where you can build your interplanetary trade empire!"
    print(banner)
    print(welcome)

# Ask the user to input the mode they wish to use
def choose_mode():
    print("Would you like to play in story mode?")
    mode = input("[y/n]: ")
    return mode

def get_seed():

    seed_string = input("Seed: ")
    # set seed here because the Random package sets the GLOBAL seed in rng.seed methods
    if seed_string == "":
        rng.seed()
    else:
        rng.seed(seed_string)

def get_seed_prompt():
    seed_text = "Please enter a number or text to seed random planet generation.  If you want a random seed, simply press 'Enter'."
    print(seed_text)
    get_seed()

def action_prompt():
    action_prompt_text = """
Enter one of the following actions:
(b)oard    (displays the network matrix)
(s)how     (show the planet information)
(h)elp     (shows this prompt)
(p)robe    (search for new planets)
(t)rade  (conenct planets together)
QUIT       (quit and exit the game)
"""
    print(action_prompt_text)

def probe_prompt(found_planets):
    # TODO: fix to show animation
    print("Probing", end="")

    # print loading elipses
    for i in range(3):
        print(".", end="")
        time.sleep(1.25)
    print() # force new line
    
    # slight delay from loading
    time.sleep(0.5)

    print("Planets have been found! Displaying found planets...")
    print()
    # TODO: display planet info in a row
    for i in range(len(found_planets)):
        print(f"Planet {i + 1}:")
        found_planets[i].summary()
        print()

    print(f"Which planet would you like to add to your trade network {[*range(1, len(found_planets) + 1)]}? If none, enter \"none\".")

    new_planet = input()

    # TODO: add error checking
    if new_planet == "none":
        return None
    else:
        return found_planets[int(new_planet) - 1]
    
def trade_prompt():
    print("Which two planets would you like to connect and begin trading?")
    p1 = input("Connect planet ")
    p2 = input("to planet ")
    return p1, p2

def show_board(network, planet_list):
    print(f"Planet state list: {[planet.state for planet in planet_list]}")

    print("Planet network:")
    for row in network:
        print(*row)

def show_planet(planet_list):
    # try:
        planet_id = input("Which planet? ")
        planet_list[int(planet_id)].summary()
    # except:
    #     print("Please enter a valid planet id.")