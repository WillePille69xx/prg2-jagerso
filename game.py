from random import randint

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
print("You can choose your speed and agility values.")
print("You have a maximum of 8 points to distribute.")
print("You may only at a maximum have 6 points in either stat.")

stats_ok = False

while stats_ok == False:
    while player_horse["speed"] < 1 or player_horse["speed"] > 6:
        player_horse["speed"] = input_int("Enter your horse's speed (max 6): ")
    while player_horse["agility"] < 1 or player_horse["agility"] > 6:
        player_horse["agility"] = input_int("Enter your horse's agility (max 6): ")
    
    if player_horse["speed"] + player_horse["agility"] == 8:
        stats_ok = True
    else:
        print("Invalid stats. Try again.")
        player_horse["speed"] = 0
        player_horse["agility"] = 0

print(player_horse)

