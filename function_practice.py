'''name = input("What is your nickname" )
starting_scores = 0
print(f"Your starting score is {starting_scores}")
print(f"Welcome to the game {name}")

energy = "5"
energy = int(energy)
energy = energy - 2

print(energy)


energy = 5
energy = energy - 2
energy = energy - 1

print(energy)



energy = 5
game_running = True

while game_running:
    energy = energy - 1
    print(energy)

    if energy == 3:
        game_running = False

def greet_player():
    print("Welcome, adventurer!")

print("The game is starting.")



def display_mission():
    print("Your mission is to find the lost lighthouse!")


display_mission()
display_mission()

def show_location(location):
    print(f"You are exploring the {location} ")

show_location("Beach")
show_location("Jungle")
show_location("Lighthouse")'''


name = input("What is your name?")

energy = int(input("What is your energy level?"))
def show_players_status(name,energy):
    print(f"Player: {name}")
    print(f"Energy: {energy}")


show_players_status(name,energy)
show_players_status(name,energy)

