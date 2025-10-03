print("Welcome to Treasure Island")
print("Your Mission is to Find the treasure")
cross_road = input("You're at a cross road . Where do you want to go?\n Type 'left' or 'right'")
if cross_road == 'left':
    lake = input("You've come to a lake . There is an island in the middle of the lake."
          " \n Type 'wait' to wait for the boat. Type 'swim' to swim across")
    if lake == 'wait':
        house = input("You arrive at the island unharmed . There is a house with 3 doors.\n"
                      "One red , one yellow and one blue . Which colour do you choose?")
        if house == 'red':
            print("It's a room full of fire . Game Over")
        elif house == 'yellow':
            print("You found the treasure ! You Win !")
        else:
            print("You enter a room of beats . Game Over")
    else :
        print("You get attacked by an angry trout . Game Over")


elif cross_road == 'right':
    print("You fell into a hole .  Game Over")

