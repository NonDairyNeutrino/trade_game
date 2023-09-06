# planet class

import random as rng

RESOURCE_LIST  = ["food", "water", "air", "materials", "people", "entertainment"]
NEEDS_GIVES_STATE = "NG"
NEEDS_STATE = "N_"
GIVES_STATE = "_G"
SATISFIED_STATE = "__"

class Planet:
    # TODO: add static planet count and use it as the id
    def __init__(self):
        self.name = hex(rng.randint(16**6, 16**7 - 1))[2:].upper() # make the name a 6 character hex string
        self.id   = "Come back to this"
        self.state = NEEDS_GIVES_STATE
        self.needs = {*rng.sample(RESOURCE_LIST, 2)}
        self.gives = {*rng.sample(RESOURCE_LIST, 2)}

    def summary(self):
        print(f"name: {self.name}")
        print(f"id: {self.id}")
        print(f"state: {self.state}")
        print(f"needs: {self.needs if self.needs != {} else 'needs met!'}")
        print(f"gives: {self.gives if self.gives != {} else 'gives met!'}")

    def update_state(self):
        if self.needs == {} and self.gives == {}:
            self.state = SATISFIED_STATE
        elif self.needs == {}:
            self.state = GIVES_STATE
        elif self.gives == {}:
            self.state == NEEDS_STATE
        else:
            self.state = NEEDS_GIVES_STATE

def update_needs_gives(planet_1, planet_2):
    needs_gives_intersection = planet_1.needs.intersection(planet_2.gives)
    for resource in needs_gives_intersection:
        planet_1.needs.remove(resource)
        planet_2.gives.remove(resource)

def test():
    p1 = Planet()
    p1.summary()