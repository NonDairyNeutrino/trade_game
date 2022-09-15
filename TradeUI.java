/*
Objective: Provide the front end for user interaction
Author: Nathan Chapman
Date: 8/26/2022
*/

import java.util.Scanner;
import java.util.Random;

// TODO: initally give list of actions, but then only prompt for an action.  User can use "help" to get list again.

public class TradeUI {
  public static Scanner sc = new Scanner(System.in);
  private static Random rng = new Random();

  public static void splash () {
    String splashText = "========================\n        TRADE        \n========================";
    System.out.println(splashText);
  }

  public static void welcome () {
    splash();
    System.out.println("Welcome to TRADE; where you can build your interplanetary trade empire!");
  }

  public static String chooseMode () {
    System.out.println("To begin, enter whether you want to play in 'sandbox' or 'story' mode.");
    return sc.nextLine();
  }

  // get the user input seed or generatea a random one
  public static int getSeed () {
    String seedString;
    // if they input an empty line, return a random integer
    if ((seedString = sc.nextLine()).equals("")) {
      return rng.nextInt();
    }
    // if not, return the integer value of the string they entered
    else {
      return Integer.valueOf(seedString);
    }
    // IDEA: allow for text entry and convert to integer
  }

  public static Random getRNG () {
    String seedText = "Please enter an integer seed for planet generation.  If you want a random seed, simply press 'Enter'.";
    System.out.println(seedText);    // Display seed prompt
    System.out.print("Seed: ");
    int seed = getSeed(); // get seed
    return new Random(seed);          // get planet rng
  }

  public static void actionPrompt () {
    String actPrompt = "Enter one of the following actions:\nInformation\n (b)oard/(s)tate, (h)elp/(a)ctions/(c)ontrols\nActions\n (p)robe, (d)iscover, (c)onnect\nView\n QUIT, clear.\n";
    System.out.println(actPrompt);
  }

  public static void showActions () {
    System.out.println("INFORMATION\n===========");
    System.out.println("board: displays the state of the game board.");
    System.out.println("state: performs the 'board' action.");

    System.out.println("ACTIONS\n=======");
    System.out.println("probe: potentially reveals more planets.");
    System.out.println("discover: reveals planet's properties.");
    System.out.println("connect: connects two planets and begins trade if possible.");

    System.out.println("");
  }

  private static void slip (int time) {
    try {
      Thread.sleep(time);
    }
    catch (InterruptedException e) {
      Thread.currentThread().interrupt();
    }
  }

  // add planet choice prompt
  public static int probePrompt (Planet[] newPlanets) {
    System.out.print("Probing.");
    for (int k = 0; k < 2; k++) {
      slip(1250);
      System.out.print(".");
    }
    slip(500);
    System.out.println("\nPlanets have been found! Displaying found planets...\n");
    for (int k = 0; k < newPlanets.length; k++) {
      System.out.println("Planet " + String.valueOf(k + 1) + "\n" + newPlanets[k]);
    }

    System.out.println("Which planet would you like to add to your trade network 1, 2, 3, 4? If none, enter \"none\".");
    String input;
    while (!(input = sc.nextLine()).equals("none") && !input.equals("1") && !input.equals("2") && !input.equals("3") && !input.equals("4")) {
      System.out.println("Please 1, 2, 3, 4, or none.");
    }
    if (input.equals("1") || input.equals("2") || input.equals("3") || input.equals("4")) {
      return Integer.valueOf(input) - 1;
    }
    else {
      return -1;
    }
    // IDEA: give ability to use planet ID
  }

  public static void tradePrompt (PlanetSystem board) {
    System.out.println("Which two planets would you like to trade?");
    System.out.println("Planet 1:");
    int p1 = Integer.valueOf(sc.nextLine());
    System.out.println("Planet 2:");
    int p2 = Integer.valueOf(sc.nextLine());
    board.trade(p1 - 1, p2 - 1);
  }

  public static void showBoard (PlanetSystem board) {
    board.network.forEach((row) -> System.out.println(row));
  }

}
