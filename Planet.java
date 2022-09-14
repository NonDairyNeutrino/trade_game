/*
Objective: for the structure of a planet node in the network with its needs, gives, and name
Author: Nathan Chapman
Date: 9/8/22
*/

public class Planet {
  // Instrinsic properties
  public String name;
  private int id;
  public String needsGivesState = "NG", needsState = "N_", givesState = "_G", satisfiedState = "__";
  // values of strings can be:
  // "NG" = has unmet needs, and has things to give (default state)
  // "N_" = has unmet needs, but can't give any more
  // "_G" = has needs met, but still has resources to give
  // "__" = has needs met and no more resources to give
  public String state = needsGivesState;
  private String[] resources  = {"food", "water", "air", "materials", "people", "entertainment"};

  public String[] needs = new String[2];
  public String[] gives = new String[2];

  public Planet(int id, String[] needs, String[] gives) {
    this.id = id;
    this.name = Integer.toHexString(id);
    this.needs = needs;
    this.gives = gives;
  }
}
