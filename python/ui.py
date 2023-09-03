# interface for the user to interact with the program

import random as rng
import time

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
    print("To begin, enter whether you want to play in 'sandbox' or 'story' mode.")
    mode = input()
    return mode

def get_seed():

    seed_string = input()
    # set seed here because the Random package sets the GLOBAL seed in rng.seed methods
    if seed_string == "":
        rng.seed()
    else:
        rng.seed(seed_string)

def get_seed_prompt():
    seed_text = "Please enter a number or text to seed random planet generation.  If you want a random seed, simply press 'Enter'."
    print(seed_text)
    # don't add a new line so the user enters the seed on the same line as the "Seed: " text
    print("Seed: ", end=None)
    get_seed()
    print() # force new line

def action_prompt():
    action_prompt_text = """
Enter one of the following actions:
(b)oard    (shows the network matrix)
(h)elp     (shows this prompt)
(p)robe    (search for new planets)
(s)ettle   (settle found planet)
(c)onnect  (conenct planets together)
QUIT       (quit and exit the game)
clear      (clear the terminal)
"""
    print(action_prompt_text)

def probe_prompt(found_planets):
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
    for i in range(3):
        print(f"Planet {i + 1}:")
        found_planets[i].summary()
        print()

    print(f"Which planet would you like to add to your trade network {[*range(1, len(found_planets) + 1)]}? If none, enter \"none\".")

    new_planet = input()

    # TODO: add error checking
    if new_planet == "None":
        return None
    else:
        return int(new_planet)
    
def trade_prompt():
    print("Which two planets would you like to connect and begin trading?")
    p1 = input("Connect planet ")
    p2 = input("to planet ")
    return p1, p2