/*
Objective: This program serves to execute the main gameplay loop of the text-based implementation of the Trade game.
Author: Nathan Chapman
Date: 8/26/2022
*/

/*
Outline
-------
1) Print initial prompt and introduction to the game ex. "Welcome to (text-based) Trade where you can build your interplanetary trade empire!"

2) Generate random planets via a seed.  Seed can be given or random.

2) Get user inputted actions e.g. discover, colonize, connect, trade.

2.5) TODO: Generate planets to choose from, where each planet has randomly generated needs, gives, and name

3) TODO: Implement the action on the system via the backend

4) TODO: Return board state

5) goto step 2 and loop!
------------------------
TODO: change all Slipways terminology to graph terms (node, network, etc.)

TODO: add graph planarity checking to test if routes cross
*/

import java.util.Random;

public class Trade {

  private static Random rng;

  public static void main(String[] args) {
    TradeUI.welcome(); // display welcome text
    // prompt to give flavor or not
    String mode;
    while (!(mode = TradeUI.chooseMode()).equals("story") && !mode.equals("sandbox")) {
      System.out.println("Please enter a valid choice of mode.");
    }
    if (mode.equals("story")) {
      Flavor.intro();
    }

    rng = TradeUI.getRNG(); // get rng based on seed
    PlanetSystem board = new PlanetSystem();

    String input;
    TradeUI.actionPrompt();
    while (!(input = TradeUI.sc.nextLine()).equals("QUIT")) {
      // input can be one of "probe", "discover", "connect", etc.
      switch (input) {
        // DISPLAY
        case "b":
        case "board":
        case "s":
        case "state":
          TradeUI.showBoard(board);
          break;
        case "help":
        case "actions":
        case "controls":
          TradeUI.showActions();
          break;
        case "clear":
          System.out.print("\033\143"); // clears the console
          break;
        // ACTIONS
        case "p":
        case "probe":
          System.out.println("probe out");
          break;
        case "d":
        case "discover":
          System.out.println("discover out");
          break;
        case "c":
        case "connect":
          System.out.println("connect out");
          break;
        default:
          System.out.println("Please enter a valid action.");
          break;
      }
      System.out.println();
    }
  }
}
