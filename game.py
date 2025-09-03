from random import randint
import random
import time

player_horse = {
    "name": "",
    "speed": 0,
    "agility": 0
}

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


player_horse["name"] = input("Enter your horse's name: ")
print("You're horse has the stats speed and agility")
time.sleep(1)
print("You can choose your speed and agility values.")
time.sleep(1)
print("You have a maximum of 8 points to distribute.")
time.sleep(1)
print("You may only at a maximum have 6 points in either stat.")

def input_clamp(stat_name, prompt, clamp = 6):
    while player_horse[stat_name] < 1 or player_horse[stat_name] > clamp:
        player_horse[stat_name] = input_int(prompt)
    return 0

stats_ok = False

while stats_ok == False:
    input_clamp("speed", "Enter your horse's speed (max 6): ")
    input_clamp("agility", "Enter your horse's agility (max 6): ")

    if player_horse["speed"] + player_horse["agility"] == 8:
        stats_ok = True
    else:
        print("Invalid stats. Try again.")
        player_horse["speed"] = 0
        player_horse["agility"] = 0



def create_comp_horse():
    speed = randint(2, 6)
    name_parts = ["AI", "Lord", "Thunder", "Evil", "Shadow", "Phantom", "Nightmare", "URLoser",
                  "Dark", "Cloud", "Cypher", "Cyborg", "Stupid", "Heavenly", "Demon", "Demonic"]
    comp_horse = {
        "name": random.choice(name_parts) + " " + random.choice(name_parts), 
        "speed": speed,
        "agility": 8 - speed
    }
    return comp_horse

comp_horse = create_comp_horse()
print("____________________________________________________")
print(player_horse)
time.sleep(1)
print("-----------\!Versus!/-----------")
time.sleep(1)
print(comp_horse)
print("____________________________________________________")

def game_turn():
    player_speed = player_horse["speed"] + randint(1, 6)
    player_agility = randint(1, 6) - player_horse["agility"]
    if player_agility  >= 0:
        player_speed -= player_agility
    comp_speed = comp_horse["speed"] + randint(1, 6)
    comp_agility = randint(1, 6) - comp_horse["agility"]
    if comp_agility >= 0:
        comp_speed -= comp_agility

    time.sleep(1)
    print(f"Player horse {player_horse['name']} Sprints {player_speed} steps!")
    time.sleep(.5)
    print(f"Computer horse {comp_horse['name']} Sprints {comp_speed} steps!")

    return player_speed, comp_speed

player_steps = 0
comp_steps = 0

for i in range(10):
    steps = game_turn()
    player_steps += steps[0]
    comp_steps += steps[1]

print(f"Number of steps: {player_horse['name']} {player_steps}, {comp_horse['name']} {comp_steps}")
