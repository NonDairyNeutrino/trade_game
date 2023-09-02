# planet class

import random as rng

resources_list  = ["food", "water", "air", "materials", "people", "entertainment"];
needs_gives_state = "NG"
needs_state = "N_"
gives_state = "_G"
satisfied_state = "__";

class Planet:
    # TODO: add static planet count and use it as the id
    def __init__(self):
        self.name = hex(rng.randint(16**6, 16**7 - 1))[2:].upper() # make the name a 6 character hex string
        self.id   = "Come back to this"
        self.state = needs_gives_state
        self.needs = rng.sample(resources_list, 2)
        self.gives = rng.sample(resources_list, 2)

def test():
    p1 = Planet()
    print(f"name: {p1.name}", f"id: {p1.id}", f"state: {p1.state}", f"needs: {p1.needs}", f"gives: {p1.gives}", sep="\n")