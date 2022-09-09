/*
Objective: for the structure of a planet node in the network with its needs, gives, and name
Author: Nathan Chapman
Date: 9/8/22
*/

// TODO: add set of available resources

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class Planet {
  // Instrinsic properties
  public String name; // randomly generated hex number
  public int id;
  private String needsGives = "NG", needs = "N_", gives = "_G", satisfied = "__";
  // values of strings can be:
  // "NG" = has unmet needs, and has things to give (default state)
  // "N_" = has unmet needs, but can't give any more
  // "_G" = has needs met, but still has resources to give
  // "__" = has needs met and no more resources to give
  public String state = needsGives;
  private HashSet<String> resources  = new HashSet<String>(); // TODO: instantiate the resources HashSet with immediate collection of resource strings

  public ArrayList<String> needsList = new ArrayList<String>();
  public ArrayList<String> givesList = new ArrayList<String>();

  public Planet(int id) {
    this.id = id;
  }

  public void discover () {
    this.needs = needs;
    this.gives = gives;
  }

  public static void main(String[] args) {
    System.out.println("test");
  }

}
