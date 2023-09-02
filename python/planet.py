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

    def summary(self):
        print(f"name: {self.name}")
        print(f"id: {self.id}")
        print(f"state: {self.state}")
        print(f"needs: {self.needs}")
        print(f"gives: {self.gives}")

def test():
    p1 = Planet()
    print(p1.summary())