# planet class

import random as rng

resources_list  = ["food", "water", "air", "materials", "people", "entertainment"]
needs_gives_state = "NG"
needs_state = "N_"
gives_state = "_G"
satisfied_state = "__"

class Planet:
    # TODO: add static planet count and use it as the id
    def __init__(self):
        self.name = hex(rng.randint(16**6, 16**7 - 1))[2:].upper() # make the name a 6 character hex string
        self.id   = "Come back to this"
        self.state = needs_gives_state
        self.needs = {*rng.sample(resources_list, 2)}
        self.gives = {*rng.sample(resources_list, 2)}

    def summary(self):
        print(f"name: {self.name}")
        print(f"id: {self.id}")
        print(f"state: {self.state}")
        print(f"needs: {self.needs if self.needs != {} else 'needs met!'}")
        print(f"gives: {self.gives if self.gives != {} else 'gives met!'}")

    def update_state(self):
        if self.needs == {} and self.gives == {}:
            self.state = satisfied_state
        elif self.needs == {}:
            self.state = gives_state
        elif self.gives == {}:
            self.state == needs_state
        else:
            self.state = needs_gives_state

def update_needs_gives(planet_1, planet_2):
    needs_gives_intersection = planet_1.needs.intersection(planet_2.gives)
    for resource in needs_gives_intersection:
        planet_1.needs.remove(resource)
        planet_2.gives.remove(resource)

def test():
    p1 = Planet()
    p1.summary()