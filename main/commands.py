'''
commands.py holds the functions for each of the commands in the game. 
Each command is a function that takes in the player and location objects, 
as well as any additional arguments needed for the command. 
The functions are called from the main game loop in game.py.
'''

import time

# TALK to characters
def talk(location, character_name):
    # find the character to talk to    
    for character in location.characters:
        if character.name.lower() == character_name:
            # print that character's current dialogue node
            character.print_dialogue()
            time.sleep(1)
            return
    # character not found in room
    print(character_name + " is not here.")
    time.sleep(1)

# LOOK at items, characters, or the room
def look(player, location, look_at):
    # if the player wants to look at the room, they can just type "look room" or "look [room name]"
    if look_at == 'room':
        look_at = player.location.name.casefold()

    # print the long description of the room if the player looks at the room
    if look_at == location.name.casefold():
        for line in location.long_description:
            print(line)
            time.sleep(1)
        # print items in the room
        location.print_items_in_room()
        return

    # check if the player wants to look at a character in the room
    # print character description
    for character in location.characters:
        if look_at == character.name.casefold():
            character.print_character_description()
            return
    
    # player must have looked at the room first before looking at items in room
    if location.looked_at:
        for item in location.items:
            if look_at == item.name.casefold():
                item.look_item()
                return

    # look at an item in player's inventory
    for item in player.inventory:
        if look_at == item.name.casefold():
            item.look_item()
            return

    # if the player has not looked at the room yet, they cannot look at items in the room
    print("There is no '" + look_at + "' to look at.")
    time.sleep(1)

# MOVE to a different room
def move(player, location, direction):
    if direction == 'n':
        direction = 'north'
    if direction == 's':
        direction = 'south'
    if direction == 'e':
        direction = 'east'
    if direction == 'w':
        direction = 'west'

    # player entered an invalid direction, keep asking for a valid direction until they enter one
    while direction not in location.connections:
        print("You cannot move " + direction + " from here.")
        time.sleep(1)
        location.print_viable_moves()
        time.sleep(1)
        direction = input("Which direction do you want to move? ").strip().casefold()

        if direction == 'n':
            direction = 'north'
        if direction == 's':
            direction = 'south'
        if direction == 'e':
            direction = 'east'
        if direction == 'w':
            direction = 'west'

    # move the player to the new location
    new_location = location.connections[direction]
    print("You move " + direction + " into the " + new_location.name)
    player.location = new_location

    # add room to set of rooms visited
    new_location.visited = True
    player.rooms_visited.add(new_location)    
    time.sleep(1)

# Print player's INVENTORY
def inventory(player):
    player.print_inventory()
    time.sleep(1)

# GET an item from the room
def get(player, location, to_get):
    # player must have looked at room before getting items from room
    if location.looked_at:
        for item in location.items:
            if item.name.casefold() == to_get:
                # check if item is static (cannot be picked up) or not
                if not item.static:
                    player.inventory.append(item)
                    item.picked_up = True
                    item.location = None
                    location.items.remove(item)
                    item.look_item()
                    time.sleep(1)
                    print("You pick up " + item.name + " and put it in your inventory.")
                    time.sleep(1)
                    return
                else:
                    print(item.name + " cannot be picked up.")
                    time.sleep(1)
                    return

        # item is not found in the room
        print("You cannot get '" + to_get + "'.")
        time.sleep(1)
                
    else:
        print("You must first look around the room before getting anything.")
        time.sleep(1)
            
# USE an item from player's inventory or from the room
def use(player, location, object):
    # check items in the player's inventory
    for item in player.inventory:
        if item.name.casefold() == object:
            # check the item can be used
            if item.use_func:
                print("You use " + item.name + ".")
                time.sleep(1)
                item.use_item()
                time.sleep(1)
                return
            else:
                print(item.name + " cannot be used.")
                time.sleep(1)
                return

    # check items in the room
    for item in location.items:
        if item.name.casefold() == object:
            # check the item can be used
            if item.use_func:
                print("You use " + item.name + ".")
                time.sleep(1)
                item.use_item()
                time.sleep(1)
                return
            else:
                print(item.name + " cannot be used.")
                time.sleep(1)
                return

    # if the item is not found in the player's inventory or in the room
    print("'" + object + "' is not in your inventory.")
    time.sleep(1)

# Explain COMMANDS
def commands():
    print("Here is an explanation on how to use commands.")
    time.sleep(1)
    print("Valid commands are: talk, look, move, use, get, inventory, quit, and commands.")
    time.sleep(1)
    print("You can also use just the first letter of each command. So 't' is the same as 'talk', for example.")
    time.sleep(1)
    print("Some commands can take additional arguments. Talk, look, move, use, and get all can take arguments.")
    time.sleep(1)
    print("For commands that take arguments, type the command followed by the argument, with no additional filler words.")
    time.sleep(1)
    print("For example, for move, you can type 'move north' or 'm n'. For directional arguments, you can also just enter the first letter of the direction.")
    time.sleep(1)
    print("For talk, look, use, and get, the argument is the name of the character, item, or room.")
    time.sleep(1)
    print("To look around a room, you can enter 'look [room name]', or just 'look room'.")
    time.sleep(1)
    print("Commands and arguments are NOT case sensitive, but you must spell them correctly, including spaces if an argument has spaces.")
    time.sleep(1)