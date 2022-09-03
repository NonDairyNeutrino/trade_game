/*
Objective: Graph representation of the system of planets
Author: Nathan Chapman
Date: 8/7/2022
*/

import java.util.ArrayList;

public class PlanetSystem {
// CLASS VARIABLES
  public ArrayList<Planet> planets;
  public ArrayList<ArrayList<String> > network;

  private static String needsGives = "NG", needs = "N_", gives = "_G", satisfied = "__";
  // values of strings can be:
  // "NG" = has unmet needs, and has things to give (default state)
  // "N_" = has unmet needs, but can't give any more
  // "_G" = has needs met, but still has resources to give
  // "__" = has needs met and no more resources to give

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

    network.forEach((row) -> row.add("poop")); // tack on another element at the end of each row

    network.add(new ArrayList<String>(newDim)); // add an EMPTY row
    // initialize new row
    for (int k = 0; k < newDim; k++) {
      network.get(newDim - 1).add("poop"); // initialize the last row
    }
  }

  // when a
  public void addPlanet (Planet p) {
    planets.add(p);
    if (network.get(0).isEmpty()) {
      network.get(0).add(needsGives);
    }
    else {
      extendNetwork();
      System.out.println(network);
      //network.get(network.size() - 1).set(network.size() - 1, needsGives);
    }
  }

  // TODO: add  planet connecting
  public void addConnection (Planet p1, Planet p2) {
    p1.connect(p2);

  }

  // trade between planets
  public void trade(Planet p){

  }

  public void showBoard () {
    System.out.println(network);
  }

  public static void main(String[] args) {
    PlanetSystem empire = new PlanetSystem();
    empire.addPlanet(new Planet(0));
    empire.showBoard();
    empire.addPlanet(new Planet(1));
    empire.showBoard();
  }
}
