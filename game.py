"""Game rules and player data for Mystery Island: The Lost Lighthouse."""

LOCATIONS = [
    "Beach",
    "Jungle",
    "Cave",
    "Shipwreck",
    "Abandoned Village",
    "Ancient Ruins",
    "Old Bridge",
    "Lighthouse",
]

# The locations a player can travel to from each place.
PATHS = {
    "Beach": ["Jungle", "Shipwreck"],
    "Jungle": ["Beach", "Cave", "Abandoned Village"],
    "Cave": ["Jungle", "Ancient Ruins"],
    "Shipwreck": ["Beach", "Abandoned Village"],
    "Abandoned Village": ["Jungle", "Shipwreck", "Old Bridge"],
    "Ancient Ruins": ["Cave", "Old Bridge"],
    "Old Bridge": ["Abandoned Village", "Ancient Ruins"],
    "Lighthouse": ["Old Bridge"],
}

# Information about each location.
DESCRIPTIONS = {
    "Beach": (
        "Waves crash against the shore. Your boat is destroyed, "
        "and a trail of footprints leads into the jungle."
    ),
    "Jungle": (
        "Tall trees block the sunlight. Something moves between "
        "the trees, and you spot a sturdy rope near an old tree."
    ),
    "Cave": (
        "The cave is cold and dark. Ancient symbols cover its walls, "
        "and an old lantern rests beside a rock."
    ),
    "Shipwreck": (
        "A broken ship lies against the rocks. Its captain's log "
        "may reveal why the lighthouse went dark."
    ),
    "Abandoned Village": (
        "Empty houses line a narrow path. An old stranger sits "
        "outside a hut and watches you carefully."
    ),
    "Ancient Ruins": (
        "Stone pillars surround an ancient doorway. A strange "
        "riddle is carved into the stone."
    ),
    "Old Bridge": (
        "A damaged bridge stretches over a deep ravine. "
        "Without a rope, crossing it would be dangerous."
    ),
    "Lighthouse": (
        "You stand before the island's silent lighthouse. "
        "The beacon mechanism waits inside."
    ),
}


def create_player(name):
    """Create a player with starting energy and an empty inventory."""
    return {
        "name": name,
        "energy": 15,
        "location": "Beach",
        "inventory": [],
        "clues": [],
        "visited": ["Beach"],
        "decisions": {},
        "game_over": False,
        "won": False,
    }


def collect_item(player, item):
    """Add an item to the player's inventory."""
    if item in player["inventory"]:
        return f"You already have the {item}."

    player["inventory"].append(item)
    return f"You collected the {item}!"


def record_clue(player, clue):
    """Add a clue to the player's journal without duplicates."""
    if clue in player["clues"]:
        return "You have already recorded this clue."

    player["clues"].append(clue)
    return f"Clue recorded: {clue}"


def move_player(player, destination):
    """Move the player to a connected location and spend energy."""
    if destination not in LOCATIONS:
        return "That location does not exist."

    if destination not in PATHS[player["location"]]:
        return f"You cannot travel directly from {player['location']} to {destination}."

    if player["energy"] < 1:
        return "You are too exhausted to travel."

    player["energy"] -= 1
    player["location"] = destination

    if destination not in player["visited"]:
        player["visited"].append(destination)

    return f"You travelled to {destination}. Energy remaining: {player['energy']}."


def cross_old_bridge(player):
    """Cross the bridge if the player has a rope."""
    if player["location"] != "Old Bridge":
        return "You must be at the Old Bridge first."

    if "rope" not in player["inventory"]:
        return "The bridge is too dangerous! Find a rope first."

    if player["energy"] < 1:
        return "You are too exhausted to cross the bridge."

    player["energy"] -= 1
    player["location"] = "Lighthouse"

    if "Lighthouse" not in player["visited"]:
        player["visited"].append("Lighthouse")

    return "You safely crossed the bridge and reached the Lighthouse!"


def solve_ruins_puzzle(player, answer):
    """Solve the ancient riddle and award the key."""
    if player["location"] != "Ancient Ruins":
        return "You must be at the Ancient Ruins to solve the puzzle."

    if "ancient_key" in player["inventory"]:
        return "You have already solved the riddle and found the key."

    if answer.strip().lower() in ("sun", "the sun"):
        collect_item(player, "ancient_key")
        record_clue(player, "The sun is the key to the ancient doorway.")
        return "Correct! A stone door opens, revealing an ancient key."

    return "That answer is incorrect. Study the clues and try again."


def activate_beacon(player):
    """Activate the lighthouse beacon when the required items are present."""
    if player["location"] != "Lighthouse":
        return "You must reach the Lighthouse first."

    if "lantern" not in player["inventory"]:
        return "The beacon mechanism is dark. You need a lantern."

    if "ancient_key" not in player["inventory"]:
        return "The beacon mechanism is locked. You need the ancient key."

    player["won"] = True
    player["game_over"] = True

    if len(player["clues"]) >= 3 and player["decisions"].get("trusted_stranger"):
        return (
            "\nTHE SECRET ENDING\n"
            "The beacon bursts into golden light. Ships appear on the horizon, "
            "and the stranger reveals that the island's ancient guardians "
            "have been waiting for a worthy explorer. You have uncovered "
            "the island's greatest secret!"
        )

    return (
        "\nVICTORY!\n"
        "The lighthouse beacon shines across the sea. A passing ship "
        "spots the light and comes to rescue you. You have saved yourself "
        "and restored hope to the island!"
    )


def get_map(player):
    """Display discovered and undiscovered locations."""
    symbols = {
        "Beach": "🏖️",
        "Jungle": "🌴",
        "Cave": "🕳️",
        "Shipwreck": "🚢",
        "Abandoned Village": "🏚️",
        "Ancient Ruins": "🗿",
        "Old Bridge": "🌉",
        "Lighthouse": "🗼",
    }

    lines = ["", "========== ISLAND MAP =========="]

    for location in LOCATIONS:
        if location in player["visited"]:
            lines.append(f"{symbols[location]} {location}")
        else:
            lines.append("❓ Unknown location")

    lines.append("================================")
    return "\n".join(lines)


def get_journal(player):
    """Display the player's name, energy, inventory, and clues."""
    lines = [
        "",
        "========== EXPLORER'S JOURNAL ==========",
        f"Explorer: {player['name']}",
        f"Location: {player['location']}",
        f"Energy: {player['energy']}",
        f"Inventory: {', '.join(player['inventory']) or 'Empty'}",
        "",
        "Discoveries:",
    ]

    if player["clues"]:
        for number, clue in enumerate(player["clues"], start=1):
            lines.append(f"{number}. {clue}")
    else:
        lines.append("No clues discovered yet.")

    lines.append("========================================")
    return "\n".join(lines)