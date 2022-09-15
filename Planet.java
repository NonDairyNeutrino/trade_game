/*
Objective: for the structure of a planet node in the network with its needs, gives, and name
Author: Nathan Chapman
Date: 9/8/22
*/

import java.util.ArrayList;

public class Planet {

  public static String[] resources  = {"food", "water", "air", "materials", "people", "entertainment"};
  public static String needsGivesState = "NG", needsState = "N_", givesState = "_G", satisfiedState = "__";

  // Instrinsic properties
  public String name;
  private int id;
  // values of strings can be:
  // "NG" = has unmet needs, and has things to give (default state)
  // "N_" = has unmet needs, but can't give any more
  // "_G" = has needs met, but still has resources to give
  // "__" = has needs met and no more resources to give
  public String   state = needsGivesState;
  public ArrayList<String> needs = new ArrayList<String>(2);
  public ArrayList<String> gives = new ArrayList<String>(2);

  public Planet(int count, int num, ArrayList<String> needs, ArrayList<String> gives) {
    this.id    = count;
    this.name  = Integer.toHexString(num).toUpperCase();
    this.needs = needs;
    this.gives = gives;
  }

  public String toString () {
    String nameString  = "ID:    "   + name;
    String stateString = "\nState: " + state;
    String needsString = "\nNeeds: " + needs.get(0) +", " + needs.get(1);
    String givesString = "\nGives: " + gives.get(0) + ", " + gives.get(1);
    String connectionsString = "\nConnected to: " + "CONNCETIONS";
    return  nameString + needsString + givesString + "\n";
  }
}
