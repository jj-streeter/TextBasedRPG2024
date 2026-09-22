'''contains action functions to be executed during quest nodes'''

from game_objects.characters import player

# give an item to the player from a character
def give_item(character, item):
    print("*" + character.name + "hands you '" + item.name + "', and you place it in your inventory*")
    player.inventory.append(item)

# unlock a room
def unlock_room(room):
    room.unlock()

# remove an item from the player's inventory
def remove_from_inventory(item):
    player.inventory.remove(item)

# change the name of an item
def change_item_name(item, new_name):
    item.name = new_name

# change the description of an item
def change_item_description(item, new_description):
    item.description = new_description