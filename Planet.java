import java.util.ArrayList;
import java.util.Collections;

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
  public boolean discovered = false;
  public boolean colonized  = false;
  public ArrayList<String> needsList = new ArrayList<String>();
  public ArrayList<String> givesList = new ArrayList<String>();
  // Extrinsic properties
  public ArrayList<Planet> connections = new ArrayList<Planet>();

  public Planet(int id) {
    this.id = id;
  }

  public void discover () {
    this.discovered = true;
    this.needs = needs;
    this.gives = gives;
  }

  public void colonize() {
    this.colonized = true;
  }

  public void connect(Planet p) {
    this.connections.add(p);
    p.connections.add(this);
  }

  public boolean isConnected(Planet p) {
    return this.connections.contains(p);
  }

  public static void main(String[] args) {
    System.out.println("test");
  }

}
