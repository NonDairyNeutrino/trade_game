# structure for the network of planets
# follow PlanetSystem.java

from planet import Planet, update_needs_gives

def extend_network(network):
    dummy = network[-1]
    network.append(dummy) # append a row of the right length
    
    for row in network:
        row.append("")

def add_planet(planet_list, network, planet : Planet):
    planet_list.append(planet)

    if network == [[]]:
        network[0].append(planet.state)
    else:
        extend_network()
        network[-1][-1] = planet.state

def trade(network, planet_1 : Planet, planet_2 : Planet):
    # update needs and gives sets for each planet
    update_needs_gives(planet_1, planet_2)
    update_needs_gives(planet_2, planet_1)

    # update planet states
    planet_1.update_state()
    planet_2.update_state()

    # update network
    network[planet_1.id][planet_2.id] = [planet_1.state, planet_2.state]