"""Main program for Mystery Island: The Lost Lighthouse."""

from game import (
    create_player,
    collect_item,
    move_player,
    cross_old_bridge,
    solve_ruins_puzzle,
    activate_beacon,
    record_clue,
    get_map,
    get_journal,
    DESCRIPTIONS,
    PATHS,
)


def get_choice(prompt, options):
    """Ask for a valid choice and repeat until the input is accepted."""
    while True:
        choice = input(prompt).strip().lower()

        if choice in options:
            return choice

        print("That is not a valid choice. Please try again.")


def show_status(player):
    """Display the player's current status."""
    print(f"\nExplorer: {player['name']}")
    print(f"Location: {player['location']}")
    print(f"Energy: {player['energy']}")
    print(f"Inventory: {', '.join(player['inventory']) or 'Empty'}")


def travel_menu(player):
    """Let the player choose a connected location."""
    destinations = PATHS[player["location"]]

    print("\nWhere would you like to travel?")

    for number, destination in enumerate(destinations, start=1):
        print(f"{number}. {destination}")

    print("0. Stay here")

    options = [str(number) for number in range(len(destinations) + 1)]

    choice = get_choice("Choose a destination: ", options)

    if choice == "0":
        print("You decide to stay where you are.")
        return

    destination = destinations[int(choice) - 1]
    print(move_player(player, destination))


def explore_location(player):
    """Display the description and actions available at the current location."""
    location = player["location"]

    print("\n" + "=" * 55)
    print(f"📍 {location.upper()}")
    print("=" * 55)
    print(DESCRIPTIONS[location])

    if location == "Beach":
        print("\n1. Follow the footprints into the jungle")
        print("2. Search the shoreline")
        print("3. Travel")
        print("4. View map")
        print("5. Open journal")
        print("6. Quit adventure")

    elif location == "Jungle":
        print("\n1. Collect the rope")
        print("2. Investigate the footprints")
        print("3. Travel")
        print("4. View map")
        print("5. Open journal")
        print("6. Quit adventure")

    elif location == "Cave":
        print("\n1. Collect the lantern")
        print("2. Examine the wall symbols")
        print("3. Travel")
        print("4. View map")
        print("5. Open journal")
        print("6. Quit adventure")

    elif location == "Shipwreck":
        print("\n1. Search the captain's cabin")
        print("2. Search the cargo")
        print("3. Travel")
        print("4. View map")
        print("5. Open journal")
        print("6. Quit adventure")

    elif location == "Abandoned Village":
        print("\n1. Speak to the stranger")
        print("2. Search an abandoned house")
        print("3. Travel")
        print("4. View map")
        print("5. Open journal")
        print("6. Quit adventure")

    elif location == "Ancient Ruins":
        print("\n1. Solve the ancient riddle")
        print("2. Examine the inscription")
        print("3. Travel")
        print("4. View map")
        print("5. Open journal")
        print("6. Quit adventure")

    elif location == "Old Bridge":
        print("\n1. Cross the bridge")
        print("2. Travel")
        print("3. View map")
        print("4. Open journal")
        print("5. Quit adventure")

    elif location == "Lighthouse":
        print("\n1. Activate the beacon")
        print("2. Examine the lighthouse")
        print("3. View map")
        print("4. Open journal")
        print("5. Quit adventure")


def handle_action(player, choice):
    """Carry out the action selected by the player."""
    location = player["location"]

    if location == "Beach":
        if choice == "1":
            print("You follow the footprints into the jungle.")
            print(move_player(player, "Jungle"))

        elif choice == "2":
            print("You search the shoreline and discover a message in a bottle.")
            print(record_clue(player, "The lighthouse is the island's only hope."))

        elif choice == "3":
            travel_menu(player)

        elif choice == "4":
            print(get_map(player))

        elif choice == "5":
            print(get_journal(player))

        elif choice == "6":
            player["game_over"] = True
            print("You abandon the adventure.")

    elif location == "Jungle":
        if choice == "1":
            print(collect_item(player, "rope"))

        elif choice == "2":
            print("The footprints lead toward the abandoned village.")
            print(record_clue(player, "Someone has recently visited the island."))

        elif choice == "3":
            travel_menu(player)

        elif choice == "4":
            print(get_map(player))

        elif choice == "5":
            print(get_journal(player))

        elif choice == "6":
            player["game_over"] = True
            print("You abandon the adventure.")

    elif location == "Cave":
        if choice == "1":
            print(collect_item(player, "lantern"))

        elif choice == "2":
            print("The symbols show a sun above a locked doorway.")
            print(record_clue(player, "The sun symbol appears to unlock an ancient mechanism."))

        elif choice == "3":
            travel_menu(player)

        elif choice == "4":
            print(get_map(player))

        elif choice == "5":
            print(get_journal(player))

        elif choice == "6":
            player["game_over"] = True
            print("You abandon the adventure.")

    elif location == "Shipwreck":
        if choice == "1":
            print("You find the captain's log beneath a broken table.")
            print(
                record_clue(
                    player,
                    "The captain wrote that the lighthouse key lies in the Ancient Ruins.",
                )
            )

        elif choice == "2":
            print("You search the cargo and find nothing useful.")
            print("The sea has claimed almost everything.")

        elif choice == "3":
            travel_menu(player)

        elif choice == "4":
            print(get_map(player))

        elif choice == "5":
            print(get_journal(player))

        elif choice == "6":
            player["game_over"] = True
            print("You abandon the adventure.")

    elif location == "Abandoned Village":
        if choice == "1":
            if player["decisions"].get("talked_to_stranger"):
                print("The stranger has nothing more to tell you.")
            else:
                print(
                    "\nStranger: 'The island has been waiting for someone "
                    "to restore the lighthouse.'"
                )
                print("Stranger: 'Will you trust me and listen to my warning?'")

                answer = get_choice("Trust the stranger? (yes/no): ", ["yes", "no"])
                player["decisions"]["talked_to_stranger"] = True

                if answer == "yes":
                    player["decisions"]["trusted_stranger"] = True
                    print(
                        record_clue(
                            player,
                            "The stranger says the sun opens the ancient door.",
                        )
                    )
                else:
                    player["decisions"]["trusted_stranger"] = False
                    print("You decide to be cautious. The stranger falls silent.")

        elif choice == "2":
            print("Inside a house, you find an old drawing of the lighthouse.")
            print(record_clue(player, "The lighthouse beacon must be activated by hand."))

        elif choice == "3":
            travel_menu(player)

        elif choice == "4":
            print(get_map(player))

        elif choice == "5":
            print(get_journal(player))

        elif choice == "6":
            player["game_over"] = True
            print("You abandon the adventure.")

    elif location == "Ancient Ruins":
        if choice == "1":
            print("\nAncient inscription: 'I rise in the east and light the world.'")
            answer = input("What am I? ").strip()
            print(solve_ruins_puzzle(player, answer))

        elif choice == "2":
            print("The inscription warns that the beacon needs a lantern and a key.")
            print(record_clue(player, "The beacon requires a lantern and an ancient key."))

        elif choice == "3":
            travel_menu(player)

        elif choice == "4":
            print(get_map(player))

        elif choice == "5":
            print(get_journal(player))

        elif choice == "6":
            player["game_over"] = True
            print("You abandon the adventure.")

    elif location == "Old Bridge":
        if choice == "1":
            print(cross_old_bridge(player))

        elif choice == "2":
            travel_menu(player)

        elif choice == "3":
            print(get_map(player))

        elif choice == "4":
            print(get_journal(player))

        elif choice == "5":
            player["game_over"] = True
            print("You abandon the adventure.")

    elif location == "Lighthouse":
        if choice == "1":
            print(activate_beacon(player))

        elif choice == "2":
            print("Dust covers the mechanism. The lantern and key should fit.")
            print(record_clue(player, "The beacon must be unlocked before it can shine."))

        elif choice == "3":
            print(get_map(player))

        elif choice == "4":
            print(get_journal(player))

        elif choice == "5":
            player["game_over"] = True
            print("You abandon the adventure.")


def get_location_choice(player):
    """Get a valid action for the player's current location."""
    location = player["location"]

    if location in ("Beach", "Jungle", "Cave", "Shipwreck",
                    "Abandoned Village", "Ancient Ruins"):
        options = ["1", "2", "3", "4", "5", "6"]

    elif location == "Old Bridge":
        options = ["1", "2", "3", "4", "5"]

    else:
        options = ["1", "2", "3", "4", "5"]

    return get_choice("\nWhat would you like to do? ", options)


def play_game():
    """Run one complete adventure."""
    print("\n" + "=" * 55)
    print("       MYSTERY ISLAND: THE LOST LIGHTHOUSE")
    print("=" * 55)

    name = input("\nWhat is your name, explorer? ").strip()

    while not name:
        print("Your explorer needs a name!")
        name = input("Please enter your name: ").strip()

    player = create_player(name)

    print(f"\nWelcome, {player['name']}!")
    print(
        "A terrible storm has destroyed your boat. You are stranded "
        "on a mysterious island."
    )
    print(
        "Your mission is to discover the island's secrets and restore "
        "the lighthouse beacon before your energy runs out."
    )
    print("\nExplore carefully. Your decisions matter!")

    while not player["game_over"]:
        if player["energy"] <= 0:
            player["game_over"] = True
            print("\nYou collapse from exhaustion. The island remains a mystery.")
            print("GAME OVER")
            break

        show_status(player)
        explore_location(player)
        choice = get_location_choice(player)
        handle_action(player, choice)

    if player["won"]:
        print("\nCongratulations, explorer!")

    print(get_journal(player))


def main():
    """Allow the player to replay the adventure."""
    while True:
        play_game()

        answer = get_choice(
            "\nWould you like to play again? (yes/no): ",
            ["yes", "no"],
        )

        if answer == "no":
            print("\nThank you for playing Mystery Island: The Lost Lighthouse!")
            print("Goodbye, explorer!")
            break


if __name__ == "__main__":
    main()