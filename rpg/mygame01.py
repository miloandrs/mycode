#!/usr/bin/env python3
"""
RPG Game
"""


#Run-time code
def main():
    def showInstructions():
        """Show the game instructions when called"""
        #print a main menu and the commands
        print('''
        RPG Game
        ========
        Commands:
        go [direction]
        get [item]
        ''')

    def showStatus():
        """determine the current status of the player"""
        # print the player's current location
        print('---------------------------')
        print('You are in the ' + currentRoom)
        # print what the player is carrying
        print('Inventory:', inventory)
        # check if there's an item in the room, if so print it
        if 'item' in rooms[currentRoom]:
            print(f'You see  {rooms[currentRoom]["item"]}')
            print("---------------------------")


    # an inventory, which is initially empty
    inventory = []

    # a dictionary linking a room to other rooms
    rooms = {

                'Hall' : {
                    'south' : 'Kitchen',
                    'west'  : 'Bedroom'
                    },

                'Kitchen' : {
                    'north' : 'Hall',
                    'west'  : 'Bathroom',
                    'item'  : ['TrailMix_Bag', 'Yogurt']
                    },
                    
                'Bedroom' : {
                    'east' : 'Hall',
                    'south'  : 'Bathroom',
                    'item'  : ['Pistol', 'Pistol_rounds']
                    },

                'Bathroom' : {
                    'north' : 'Hall',
                    'east'  : 'Kitchen',
                    'item'  : ['Medicine', 'Zombie']
                    }

            }

    # start the player in the Hall
    currentRoom = 'Hall'

    showInstructions()

    # breaking this while loop means the game is over
    while True:
        showStatus()

        # the player MUST type something in
        # otherwise input will keep asking
        move = ''
        while move == '':  
            move = input('>')

        # normalizing input:
        # .lower() makes it lower case, .split() turns it to a list
        # therefore, "get golden key" becomes ["get", "golden key"]          
        move = move.lower().split(" ", 1)

        #if they type 'go' first
        if move[0] == 'go':
            #check that they are allowed wherever they want to go
            if move[1] in rooms[currentRoom]:
                #set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
            # if they aren't allowed to go that way:
            else:
                print('You can\'t go that way!')

        #if they type 'get' first
        if move[0] == 'get' :
            # make two checks:
            # 1. if the current room contains an item
            # 2. if the item in the room matches the item the player wishes to get
            if "item" in rooms[currentRoom]: #and move[1] in rooms[currentRoom]['item']:
                #add the item to their inventory
                inventory.extend(rooms[currentRoom]['item'])
                #display a helpful message
                print(f'got {rooms[currentRoom]["item"]}')
                #delete the item key:value pair from the room's dictionary
                del rooms[currentRoom]['item']
            # if there's no item in the room or the item doesn't match
            else:
                #tell them they can't get it
                print('Can\'t get ' + move[1] + '!')
        
        #if the player enters the room with the Zombie
        if 'item' in rooms[currentRoom] and 'Zombie' in rooms[currentRoom]['item']:
            showStatus()
            print('In this game, the zombies enjoy improvised parfair desert. Do you have Ingredients?')
            print('You can make a parfait or attack it!')
            if 'TrailMix_Bag' and 'Yogurt' in inventory:
                print("You made a parfair and the Zombie left you alone.")
            elif 'Pistol' and 'Pistol_rounds' in inventory:
                print("Attack it is!")
                print("BANG, BANG!!")
                print("Was this really necessary? how could you??")
            else:
                print("The Zombie ate your brain... #sadness")
                break







#Call main function
if __name__ == "__main__":
    main()
