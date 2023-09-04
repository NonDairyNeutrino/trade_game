# structure for the network of planets
# follow PlanetSystem.java

from planet import Planet, update_needs_gives

def extend_network(network):
    new_row = ["" for i in range(len(network))]
    network.append(new_row) # append a row of the right length
    
    for row in network:
        row.append("")

def add_planet(planet_list, network, planet : Planet):
    planet.id = len(planet_list)
    planet_list.append(planet)
    extend_network(network)

def connect(network, planet_1 : Planet, planet_2 : Planet):
    network[planet_1.id][planet_2.id] = [planet_1.state, planet_2.state]
    network[planet_2.id][planet_1.id] = [planet_2.state, planet_1.state]

def trade(network, planet_1 : Planet, planet_2 : Planet):
    if planet_1 is not planet_2:
    # update needs and gives sets for each planet
        update_needs_gives(planet_1, planet_2)
        update_needs_gives(planet_2, planet_1)

        # update planet states
        planet_1.update_state()
        planet_2.update_state()

        # update network
        connect(network, planet_1, planet_2)
    else:
        print("Planets cannot trade with themselves.")