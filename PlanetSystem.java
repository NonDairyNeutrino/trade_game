/*
Objective: Graph representation of the system of planets
Author: Nathan Chapman
Date: 8/7/2022
*/

import java.util.ArrayList;
import java.util.Random;

public class PlanetSystem {
// CLASS VARIABLES
  public ArrayList<Planet> planets;
  public ArrayList<ArrayList<String> > network;
  public int planetCount = 0;

// METHODS
  // create an empty planetary system
  public PlanetSystem () {
    // initialize system with 0 planets
    planets = new ArrayList<Planet>();
    // initialize system with a null network adjacency matrix
    network = new ArrayList<ArrayList<String> >();
    network.add(new ArrayList<String>());
  }

  // add a new row and column to the network adjacency matrix
  private void extendNetwork () {
    int curDim = network.size();
    int newDim = network.size() + 1;

    network.forEach((row) -> row.add("")); // tack on another element at the end of each row

    network.add(new ArrayList<String>(newDim)); // add an EMPTY row
    // initialize new row
    for (int k = 0; k < newDim; k++) {
      network.get(newDim - 1).add(""); // initialize the last row
    }
  }

  // when a
  public void addPlanet (Planet p) {
    planets.add(p);
    if (network.get(0).isEmpty()) {
      network.get(0).add(p.state);
    }
    else {
      extendNetwork();
      network.get(network.size() - 1).set(network.size() - 1, p.state);
    }
  }

  // gets new planets
  public Planet[] probe (Random rng) {
    Planet[] newPlanets = new Planet[4];
    for (int k = 0; k < newPlanets.length; k++) {
      int num = 16777216 + rng.nextInt(251658240); // 16^6 + [0, 16^7 - 16^6)
      String[] needs = {Planet.resources[rng.nextInt(4)], Planet.resources[rng.nextInt(4)]};

      String[] gives = {Planet.resources[rng.nextInt(4)], Planet.resources[rng.nextInt(4)]};

      newPlanets[k] = new Planet(planetCount++, num, needs, gives);
    }
    return newPlanets;
  }

  // TODO: add  planet connecting
  public void addConnection (Planet p1, Planet p2) {


  }

  // trade between planets
  public void trade(Planet p){

  }
}
