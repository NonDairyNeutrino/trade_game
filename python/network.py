# structure for the network of planets
# follow PlanetSystem.java

from planet import Planet, update_needs_gives

def extend_network(network : list[list[bool]]):
    """
    extend_network() in-place modifies a given network matrix to have one more row and one more column.
    """
    new_row = [0 for i in range(len(network))]
    network.append(new_row) # append a row of the right length
    
    for row in network:
        row.append(0)

def add_planet(planet_list : list[Planet], network : list[list[bool]], planet : Planet) -> None:
    """
    Adds a planet to planet_list and the network matrix.  Additionally assigns the planet id as the planet count.
    """
    planet.id = len(planet_list)
    planet_list.append(planet)
    extend_network(network)

def connect(network : list[list[bool]], planet_1 : Planet, planet_2 : Planet):
    """
    Changes the appropriate network matrix values to represent a connection.
    """
    network[planet_1.id][planet_2.id] = 1
    network[planet_2.id][planet_1.id] = 1

def trade(network : list[list[bool]], planet_1 : Planet, planet_2 : Planet):
    """
    Updates the network matrix via 'connect', updates each planets needs, gives, and state to match trading.
    """
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