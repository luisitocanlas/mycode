#!/usr/bin/python3

# imports
import random
import os
import time

# character and monster properties
# TODO incorporate monster properties inside dictionary or put monsters in own dictionary
characterHP = 50
enemyHP = 50
listOfAttacks = ['punch', 'kick', 'elbow', 'knee']

#an inventory, which is initially empty
inventory = []

# A dictionary linking a room to other rooms
rooms = {
        'Wreckage' :{
                    'forward' : 'Coastline',
                    'item'   : 'club'
                    },
        'Coastline':{
                    'forward' : 'Beach',
                    'back'   : 'Wreckage',
                    'item'   : 'potion'
                    },
        'Beach' :{
                    'forward': 'Settlement',
                    'back'   : 'Coastline',
                    'monster': 'Hillock'
                    },
        'Settlement':{
                    'back'   : 'Beach'
                    }
        }

def showInstructions():
    #print a main menu and the commands
    print('''
    Introduction to Path of Exile
    ========
    Commands:
    go [direction] (forward or back)
    get [item]
    use [item]
    fight [monster]
    ''')
    print("") # just a blank line
    print('''
    Welcome to Wraeclast, Exile. 
        You find yourself washed ashore on the coast, 
        battered and broken from the treacherous sea. 
        But don't be fooled by the tranquil surroundings, 
        for this land is cursed with dark magic and home to unspeakable horrors.
        ''')
    
def showStatus():
    #print the player's current status
    print('\n---------------------------')
    print(f"You are in the {currentRoom}")
  
    #print the current HP
    print(f"Your HP : {characterHP}")

    #print the current inventory
    print(f"Inventory : {inventory}")

    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print(f"There\'s a {rooms[currentRoom]['item']} on the ground")

    #print a monster if there is one
    if 'monster' in rooms[currentRoom]:
        print(f"{rooms[currentRoom]['monster']} slowly walks towards you...")
        print(f"{rooms[currentRoom]['monster']}'s HP : {enemyHP}")
    print("---------------------------\n")

# TODO make functions fight(), item()

# TODO Implement def main() starting here

#start the player in the Wreckage
os.system('clear')
currentRoom = 'Wreckage'

showInstructions()

# implement some user input here before proceeding
input("Press any key to continue...")

#loop forever
while True:
    # os.system('clear')

    # pause for effect
    time.sleep(0.5)

    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':
        print("What will you do?")
        move = input('> ')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    #if they type 'use' first
    if move[0] == 'use':
        if move[1] in inventory and move[1] == 'potion':
            # what happens if you have full health
            if characterHP == 50:
                print("You just wasted a potion!")
                inventory.remove('potion')
            # what happens when the potion heals more than your max HP
            elif characterHP >= 26:
                print("You regained some HP!")
                characterHP = 50
                inventory.remove('potion')
            # normal HP
            else:
                print("You regained some HP!")
                characterHP += 25
                inventory.remove('potion')
        else:
            print("You don't have anything to use!")

    #if they type 'fight' first
    if move[0] == 'fight':
        #check if there's a monster
        if 'monster' in rooms[currentRoom] and move[1].title() in rooms[currentRoom]['monster']:
            # character turn
            if 'club' in inventory:
                print("You used the club to attack!")
                enemyHP -= random.randint(5,10)
            else:
                print(f"You {random.choice(listOfAttacks)}ed {rooms[currentRoom]['monster']}!")
                enemyHP -= random.randint(1,6)

            # check if you defeat the monster
            if enemyHP <= 0:
                enemyHP = 0
                print(f"You defeated {rooms[currentRoom]['monster']}!")
                del rooms[currentRoom]['monster']     

            # opponent turn
            if enemyHP > 0:
                print(f"{rooms[currentRoom]['monster']} {random.choice(listOfAttacks)}ed you!")
                characterHP -= random.randint(3,8)

            # check if you are defeated
            if characterHP <= 0:
                characterHP = 0
                print(f"\n{rooms[currentRoom]['monster']} got the best of you.")
                
        else:
            print(f"Can\'t fight {move[1]}!")

    # something for when you enter the Settlement
    if currentRoom == 'Settlement' and enemyHP > 0:
        print("A group of exiles is blocking the entrance to the settlement.")
        print("Hold up there, Exile. You won't be seeing Lioneye's Watch until that foul bastard on the beach is dead and buried.")
        currentRoom = rooms[currentRoom]['back']

    ## Win conditions
    if currentRoom == 'Settlement' and enemyHP == 0:
        print("You entered the safety of Lioneye's Watch.")
        print("Now begins your true journey Exile!")
        print("Congratulations! You've beaten the game!")
        break

    ## Game Over
    if characterHP <= 0:
        print("Not today Exile!")
        print("Game Over")
        break

# TODO if __name__ == '__main__'